import os,sys;
import numpy as np;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from networksecurity.constants.modelTrainerConfig import ModelTrainerConfig;
from networksecurity.constants.dataTransformationConfig import DataTransformationConfig;
from networksecurity.utils.npFileUtil import load_numpyArray_data;
from networksecurity.utils.pickleFileUtil import load_pickle_file,save_pickle_file;
from networksecurity.utils.yamlFileUtil import save_yaml_file;
from networksecurity.components.networkSecurityModel import NetworkSecurityModel;
from sklearn.linear_model import LogisticRegression;
from sklearn.tree import DecisionTreeClassifier;
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier;
from sklearn.model_selection import GridSearchCV;
from sklearn.metrics import r2_score,f1_score,recall_score,precision_score;
import mlflow;
from typing import Dict;
import warnings;
# import dagshub




class ModelTraining:
    #### This class is responsible for Model Training
    def __init__(self):
        ### Constructor
        try:
            self.__config=ModelTrainerConfig()
            self.__dataTransformationConfig=DataTransformationConfig()
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_model_training(self,train_datapath:str,test_datapath:str):
        ##### This method is responsible for performing model training
        try:
            # dagshub.init(repo_owner='TamalKoley', repo_name='MLProject_NetworkSecurity', mlflow=True)
            warnings.filterwarnings('ignore');
            logging.info("Starting Model Training")
            train_df=load_numpyArray_data(filepath=train_datapath)
            test_df=load_numpyArray_data(filepath=test_datapath)

            x_test=test_df[:,:-1]
            y_test=test_df[:,-1]

            x_train=train_df[:,:-1]
            y_train=train_df[:,-1]

            self.__train_model(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test)
  
            logging.info("Model Training Completed")
        except Exception as e:
            raise CustomException(e,sys);


    def __train_model(self,x_train:np.ndarray,y_train:np.ndarray,x_test:np.ndarray,y_test:np.ndarray):
        ####### this method is responsible for training the different models
        try:
            logging.info("Actual Model training started")
            models={
                "LogisticRegression" : LogisticRegression(),
                "DecisionTree" : DecisionTreeClassifier(),
                "RandomForest" : RandomForestClassifier(),
                "AdaBoost" : AdaBoostClassifier(),
                "GradientBoost" : GradientBoostingClassifier()
            }
            params={
                "LogisticRegression" : {

                },
                "DecisionTree" : {
                    "criterion" : ['gini', 'entropy', 'log_loss'],
                    "max_depth" :[5,7,13,17,25,30],
                    "max_features" : [3,5,7,9,15,20],
                    "min_samples_split" : [1,3,5,7]
                },
                "RandomForest" : {
                    "n_estimators" : [25,50,100,200],
                    "criterion" : ['gini', 'entropy', 'log_loss'],
                    "max_depth" : [5,7,9,13,20],
                    "min_samples_split" : [1,3,5,7]
                },
                "AdaBoost" : {
                    "n_estimators" : [25,50,100,200],
                    "learning_rate" : [1.0,0.1,0.01,0.001]
                },
                "GradientBoost" : {
                    "loss" : ['log_loss', 'exponential'],
                    "learning_rate" : [1.0,0.1,0.01,0.001] ,
                    "n_estimators" : [25,50,100,200],
                    "criterion" : ['friedman_mse', 'squared_error']
                }
            }
            
            os.makedirs(self.__config.model_training_dir,exist_ok=True)
            report=self.__evaluate_model(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models,params=params)
            best_score=-99999;
            best_model_name='';
            best_params={};
            for model_name in report.keys():
                if report[model_name]["score"]>best_score:
                    best_score=report[model_name]["score"]
                    best_model_name=model_name;
                    best_params=report[model_name]["params"];
            save_yaml_file(data=report,filepath=self.__config.hyp_result_filepath)
            logging.info("Actual Model training completed and training report saved")

            logging.info("Classification Report creation and saving started with best model and best params")
            model=models[best_model_name]
            y_train_pred=model.predict(x_train)
            y_test_pred=model.predict(x_test)
            train_cls_report=self.__get_classification_score(y_true=y_train,y_pred=y_train_pred)
            test_cls_report=self.__get_classification_score(y_true=y_test,y_pred=y_test_pred)

            ###MLFLOW tracking
            self.__track_mlflow(bestmodel=model,classification_report=train_cls_report)
            self.__track_mlflow(bestmodel=model,classification_report=test_cls_report)

            final_classification_report={
                "Model name" : best_model_name,
                "Best Params": best_params,
                "Training_Data" : train_cls_report,
                "Test_Data" : test_cls_report
            }
            save_yaml_file(data=final_classification_report,filepath=self.__config.classification_report_filepath)
            logging.info("Classification Report creation and saving completed with best model and best params")

            logging.info("Saving preprocessor and model")
            preprocessor=load_pickle_file(self.__dataTransformationConfig.trasformer_filepath)
            netsec_model=NetworkSecurityModel(model=model,preprocessor=preprocessor)
            
            os.makedirs(self.__config.transformed_object_dir,exist_ok=True)
            save_pickle_file(filepath=self.__config.transformed_model_filepath,data=netsec_model)
            os.makedirs(self.__config.final_model_dir,exist_ok=True)
            save_pickle_file(filepath=self.__config.final_model_filepath,data=netsec_model)
            logging.info("preprocessor and model saved")
            
        except Exception as e:
            raise CustomException(e,sys);

    def __evaluate_model(self,x_train:np.ndarray,y_train:np.ndarray,x_test:np.ndarray,y_test:np.ndarray,models:Dict,params:Dict)->Dict:
        ##### This method will iterate through all the models and perform training and evaluation for each type and return
        ##### a evalution report
        try:
            report={};
            for model_name in models.keys():
                logging.info(f"Evaluating Model for {model_name}")
                model=models[model_name]
                param=params[model_name]
                if model_name!="LogisticRegression":
                    grid_model=GridSearchCV(estimator=model,param_grid=param,n_jobs=-1,cv=5,verbose=2)

                    grid_model.fit(x_train,y_train)
                    best_params=grid_model.best_params_
                    model.set_params(**best_params)
                model.fit(x_train,y_train)

                #y_train_pred=model.predict(x_train)
                y_test_pred=model.predict(x_test)

                model_score=r2_score(y_test,y_test_pred)

                if model_name!="LogisticRegression":
                    report[model_name]={
                        "score" : model_score,
                        "params" : best_params
                    }
                else:
                    report[model_name]={
                        "score" : model_score,
                        "params" : {}
                    }
                logging.info(f"Model  Evaluation is completed for {model_name}")

            return report;

        except Exception as e:
            raise CustomException(e,sys)
        
    def __get_classification_score(self,y_true:np.ndarray,y_pred:np.ndarray)-> Dict:
        ##### This method is responsible for creating classification report based on predictions
        try:
            logging.info("starting generation of classification report")
            #classification_report={};
            f1Score=f1_score(y_true,y_pred)
            recallscore=recall_score(y_true,y_pred)
            r2score=r2_score(y_true,y_pred)
            precisionscore=precision_score(y_true,y_pred)
            classification_report={
                "f1_score" : f1Score,
                "recall_score" : recallscore,
                "r2_score" : r2score,
                "Precision_score" : precisionscore
            }
            logging.info("Generation of classification report is completed")
            return classification_report;
        except Exception as e:
            raise CustomException(e,sys);

    def __track_mlflow(self,bestmodel,classification_report:Dict):
        #### This method is responsible for tracking mlflow
        try:
            logging.info("mlflow tracking started")
            with mlflow.start_run():
                f1score=classification_report["f1_score"]
                recallscore=classification_report["recall_score"]
                r2score=classification_report["r2_score"]
                precisionscore=classification_report["Precision_score"]

                mlflow.log_metric("f1_score",f1score)
                mlflow.log_metric("recall_score",recallscore)
                mlflow.log_metric("r2_score",r2score)
                mlflow.log_metric("Precision_score",precisionscore)
                mlflow.sklearn.log_model(bestmodel,"model")
            logging.info("mlflow tracking completed")
        except Exception as e:
            raise CustomException(e,sys)