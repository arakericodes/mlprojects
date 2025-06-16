import sys
import logging

class Errors():
    def error_message_detail(self, error):
        error_detail = sys.exc_info()
        _,_,exc_tb=error_detail
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"Error Occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{error}]"
        return error_message

class CustomException(Errors, Exception):
    def __init__(self, err):
        super().__init__()
        print(self.error_message_detail(err))