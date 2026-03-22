import sys;

class CustomException(Exception):
    #### This class is responsible for creating custom exception with error details and place of occurence
    def __init__(self, error_message,error_details:sys):
        _,_,tb=error_details.exc_info();
        self.__lineno=tb.tb_lineno;
        self.__filename=tb.tb_frame.f_code.co_filename;
        self.__error_msg=error_message

    def __str__(self):
        return f'Exception occured at lineno {self.__lineno} on file {self.__filename} with message {self.__error_msg}'