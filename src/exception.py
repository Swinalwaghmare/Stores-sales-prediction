import sys
from src.logger import logging

def error_message_details(error,error_details:sys):
    _,_,exc_tab = error_details.exc_info()
    
    file_name = exc_tab.tb_frame.f_code.co_filename
    line_number = exc_tab.tb_frame.f_lineno
    
    error_message = f"""
                    Error occured in script: [{file_name}] 
                    at line : [{line_number}] 
                    error message: [{error}]
                    """
        
    return error_message

class StoresSalesException(Exception):
    
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)
        
    def __str__(self):
        return self.error_message
    
    

        
        
