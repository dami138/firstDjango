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
            return Response(dict(msg="로그인 실패"))
        else:
            return Response(dict(msg="로그인 성공",user_id=user.user_id, nickname = user.nickname, age =user.age))




class RegistUser(APIView):
    def post(self, request):
        # user_id = request.data.get("user_id","")
        # user_pw = request.data.get("user_pw","")
        # nickname = request.data.get("nickname", "")
        # age = request.data.get("age", 20)
        serializer = LoginUserSerializer(request.data)

        # if user_id 특수문자 숫자 한글,,, 처리 필요,,

        # 동일한 유저아이디가 있는지 검사
        if LoginUser.LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
            return Response(dict(msg="동일 아이디 있음"))

        else:
            user = serializer.create(request.data)

            #비밀번호 암호화 코드 필요,,
            # user_pw_encryted = make_password(user_pw)
            # LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encryted, nickname= nickname, age = age)

        return Response(data = LoginUserSerializer(user).data)