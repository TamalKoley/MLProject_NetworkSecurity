import sys;

class CustomException(Exception):
    def __init__(self, error_message,error_details:sys):
        _,_,tb=error_details.exc_info();
        self.__lineno=tb.tb_lineno;
        self.__filename=tb.tb_frame.f_code.co_filename;
        self.__error_msg=error_message

    def __str__(self):
        return f'Exception occured at lineno {self.__lineno} on file {self.__filename} with message {self.__error_msg}'