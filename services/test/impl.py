from codeits.log.UtilLog import UtilLog

from codeits.exceptions.ExceptionApi import ExceptionApi

import time

class ApiService:

    @staticmethod
    def echo(str_in):
        if str_in == 'raise':
            raise ExceptionApi(400,"echo 'raise' not implemented")
        return str_in
    
    @staticmethod
    def level_logs(msg):
        UtilLog.critical(msg)
        UtilLog.error(msg)
        UtilLog.warning(msg)
        UtilLog.info(msg)
        UtilLog.debug(msg)
        
        return 'OK'
    
    @staticmethod
    def stream_data():
        for i in range(0,25):
            event= "id: {}\nevent: {}\ndata: {}\n\n".format(i,'test_event', '{"id":%s, type:"test_event"}'%i)
            UtilLog.debug(event)
            yield event
            time.sleep(1)
        
        yield "id: {}\nevent: {}\ndata: {}\n\n".format(i,'test_event_close', '{}')