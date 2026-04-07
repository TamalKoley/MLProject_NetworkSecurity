import sys;
from flask import Flask,request,render_template;

import pickle;

model=pickle.load(open('Final_Models/trained_model.pkl','rb'));

app=Flask(__name__);


@app.route("/",methods=['GET','POST'])
def predict():
    try:
        print("app is staring on port 10222")
        if request.method=='POST':
            having_IP_Address=int(request.form.get('having_IP_Address'))
            URL_Length=int(request.form.get('URL_Length'))
            Shortining_Service=int(request.form.get('Shortining_Service'))
            having_At_Symbol=int(request.form.get('having_At_Symbol'))
            double_slash_redirecting=int(request.form.get('double_slash_redirecting'))
            Prefix_Suffix=int(request.form.get('Prefix_Suffix'))
            having_Sub_Domain=int(request.form.get('having_Sub_Domain'))
            SSLfinal_State=int(request.form.get('SSLfinal_State'))
            Domain_registeration_length=int(request.form.get('Domain_registeration_length'))
            Favicon=int(request.form.get('Favicon'))
            port=int(request.form.get('port'))
            HTTPS_token=int(request.form.get('HTTPS_token'))
            Request_URL=int(request.form.get('Request_URL'))
            URL_of_Anchor=int(request.form.get('URL_of_Anchor'))
            Links_in_tags=int(request.form.get('Links_in_tags'))
            sfh=int(request.form.get('SFH'))
            Submitting_to_email=int(request.form.get('Submitting_to_email'))
            Abnormal_URL=int(request.form.get('Abnormal_URL'))
            Redirect=int(request.form.get('Redirect'))
            on_mouseover=int(request.form.get('on_mouseover'))
            RightClick=int(request.form.get('RightClick'))
            popUpWidnow=int(request.form.get('popUpWidnow'))
            Iframe=int(request.form.get('Iframe'))
            age_of_domain=int(request.form.get('age_of_domain'))
            DNSRecord=int(request.form.get('DNSRecord'))
            web_traffic=int(request.form.get('web_traffic'))
            Page_Rank=int(request.form.get('Page_Rank'))
            Google_Index=int(request.form.get('Google_Index'))
            Links_pointing_to_page=int(request.form.get('Links_pointing_to_page'))
            Statistical_report=int(request.form.get('Statistical_report'))
            x=[[having_IP_Address,URL_Length,Shortining_Service,having_At_Symbol,double_slash_redirecting,
                Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length,Favicon,port,HTTPS_token,
                Request_URL,URL_of_Anchor,Links_in_tags,sfh,Submitting_to_email,Abnormal_URL,Redirect,on_mouseover,RightClick,
                popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report
                ]];
            y_pred=model.predict(x)[0];
            result='';
            if int(y_pred)==1:
                result='Phishing';
            else:
                result='NotPhising';
            return render_template('index.html',prediction=result)

        else:
            return render_template('index.html')
    except Exception as e:
        print(e)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10222)
    print("app is staring on port 10222")