from codeits.reflection.ApiEncoder import ApiEncoder

from flask import request,Response
import json

from services.test.impl import ApiService


class ApiFacade:

    @staticmethod
    def echo(str_in):
        res = ApiService.echo(str_in)
        return Response(
            response=json.dumps(res,cls=ApiEncoder),
            status=200, 
            mimetype="application/json"
        )

    @staticmethod
    def level_logs(msg):
        res = ApiService.level_logs(msg)
        return Response(
            response=json.dumps(res,cls=ApiEncoder),
            status=200, 
            mimetype="application/json"
        )
        
    @staticmethod
    def stream_data():
        return Response(
            response=ApiService.stream_data(),
            status=200,
            mimetype="text/event-stream"
        )