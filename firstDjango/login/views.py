from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
from .serialize import LoginUserSerializer


class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        user_pw = request.data.get("user_pw")

        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg="해당 아이디가 없습니다."))
        if not check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 실패, 비밀번호가 틀렸습니다."))
        else:
            return Response(dict(msg="로그인 성공",user_id=user.user_id))

class AppLogout(APIView):
    def post(self, request):
        #로그아웃한 시간 출력
        #소켓 통신을 한다면 로그아웃할때 세션을 끊게 하면 됨
        return Response(status=200)

class RegistUser(APIView):
    def post(self, request):
        #print(request.data)
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")

        #공백, 한글, 특수문자, 중복 막기
        #https://itisguide.tistory.com/21
        

        #공백불가
        if user_id =='' or user_id is None or user_pw =='' or user_pw is None:
            return Response(data=dict(msg="아이디와 비밀번호는 공백이 될 수 없습니다."))
        if user_id.find('') or user_pw.find(''):
            return Response(data=dict(msg="아이디와 비밀번호에는 공백이 들어갈 수 없습니다."))
        
        #한글불가
        if user_id.upper() == user_id.lower() or user_pw.upper() == user_pw.lower():
            return Response(data=dict(msg="아이디와 비밀번호는 한글이 들어갈 수 없으며, 숫자로만 구성할 수 없습니다."))
        
        #특수문자 불가
        if not user_id.isalnum() or not user_pw.isalnum():
            return Response(data=dict(msg="아이디와 비밀번호에는 특수문자가 들어갈 수 없습니다."))
        
        #중복불가
        if LoginUser.objects.filter(user_id=user_id).exists():
            return Response(data=dict(msg="이미 존재하는 id입니다."))

        #비밀번호 암호화
        user_pw = make_password(user_pw)

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw)

        return Response(data=dict(msg="회원가입 성공", user_id=user_id))


# 기존 코드
#
# class RegistUser(APIView):
#     def post(self, request):
#         serializer = LoginUserSerializer(request.data)
#
#         # 동일한 유저아이디가 있는지 검사
#         if LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
#             return Response(dict(msg="동일 아이디 있음"))
#
#         user = serializer.create(request.data)
#         return Response(data = LoginUserSerializer(user).data)
#

    #기존 코드
# class RegistUser(APIView):
#     def post(self, request):
#         user_id = request.data.get('user_id', "")
#         user_pw = request.data.get('user_pw', "")
#         user_pw_crypted = make_password(user_pw)    # 암호화
#
#         if LoginUser.objects.filter(user_id=user_id).exists():
#             # DB에 있는 값 출력할 때 어떻게 나오는지 보려고 user 객체에 담음
#             user = LoginUser.objects.filter(user_id=user_id).first()
#             data = dict(
#                 msg="이미 존재하는 아이디입니다.",
#                 user_id=user.user_id,
#                 user_pw=user.user_pw
#             )
#             return Response(data)
#
#         LoginUser.objects.create(user_id=user_id, user_pw=user_pw_crypted)
#
#         data = dict(
#             user_id=user_id,
#             user_pw=user_pw_crypted
#         )
#
#         return Response(data=data)