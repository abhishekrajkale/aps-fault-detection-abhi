import sys,os

def error_message_detail(error, error_detail: sys):
    pass
  



class SensorException(Exception):

     def _init_(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

     def _str_(self):
        return self.error_message