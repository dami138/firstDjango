from django.db import models

class LoginUser(models.Model):
    user_id = models.CharField(max_length=20, unique=True, null=False, default=False)
    user_pw = models.CharField(max_length=255, null=False, default=False)
    # user_pw = fields.EncryptedCharField(max_length=20, null=False, default=False)

    nickname = models.CharField(verbose_name="닉네임", max_length=20, null=False, default="")
    age = models.IntegerField(verbose_name="나이", default=20)

    class Meta:
        db_table = 'login_user'
        verbose_name = '로그인 테스트 테이블'