from rest_framework.response import Response
from rest_framework.views import APIView

class TodoView(APIView):
    user_id = ''
    version = ''

    #클라에서 post등 call 이 오면 get인지 post인지 구분
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.headers.get("id", False)
        self.version = request.headers.get("version", "1.0")
        return super(TodoView,self).dispatch(request, *args, **kwargs)

def CommonResponse(result_code, result_msg, data):
    return Response(status=200,
                    data=dict(
                        result_code=result_code,
                        result_msg=result_msg,
                        data=data
                    )
                    )

def SuccessResponse():
    return Response(status=200,
                    data=dict(
                        result_code=0,
                        result_msg="success"
                    ))

def SuccessResponseWithData(data):
    return Response(status=200,
                    data=dict(
                        result_code=0,
                        result_msg="success",
                        data=data
                    ))

def ErrorResponse():
    return Response(status=200,
                    data=dict(
                        result_code=999,
                        result_msg="error!!!"
                    ))