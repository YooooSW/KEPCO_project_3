from django.db import models, migrations
from django.utils import timezone
from django import forms
# - DB에서 varchar2 또는 char 등 문자열 타입
from django.db.models.fields import CharField
# - DB에서 숫자형 타입 자동증가
from django.db.models.fields import AutoField
# - DB에서 number 또는 integer 등 숫자형 타입
from django.db.models.fields import IntegerField
# - DB에서 날짜와 시간을 갖는 필드.
# 날짜만 가질 경우는 DateField, 시간만 가질 경우는 TimeField를 사용한다.
from django.db.models.fields import DateTimeField
# - DB에서 대용량 문자열을 갖는 필드
from django.db.models.fields import TextField
# - DB에서 파일 업로드 필드

# - user 확장
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# from django.db.models.fields import FileField
# - DB에서    FileField의 파생클래스로서 이미지 파일인지 체크
# from django.db.models.fields import ImageField
# Create your models here.

# class CustomUser(AbstractUser):
#     email = models.CharField(max_length=100)
#     phon = models.CharField(max_length=100)
#     nickname = models.CharField(max_length=100)
#     class Meta:
#         # 실제 사용할 테이블 이름 정의
#         db_table = "User"

#         # 사용할 앱 이름 정의
#         app_label = "mainapp"

#         # 외부 데이터베이스에 테이블 존재여부 확인
#         # - 존재하면 : False
#         # - 존재하지 않으면 : True
#         # --> 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
#         managed = False
# class Post(models.Model):
#     objects = models.Manager()

class User(AbstractUser):
    username = CharField(primary_key=True, max_length=20)
    password = CharField(max_length=20)
    email = CharField(max_length=100)
    phon = CharField(max_length=100)
    nickname = CharField(max_length=100)

    class Meta:
        # 실제 사용할 테이블 이름 정의
        db_table = "User"

        # 사용할 앱 이름 정의
        app_label = "mainapp"

        # 외부 데이터베이스에 테이블 존재여부 확인
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # --> 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed = False
        
# class User_img(models.Model):
#     user_num = IntegerField(primary_key=True)
#     username = models.ForeignKey(User,
#                                 to_field="username",
#                                 db_column="username",
#                                 on_delete=models.CASCADE)
#     user_path = CharField(max_length=100)
#     user_date = DateTimeField(auto_now = True)
    
#     class Meta:
#         db_table = "User_img"

#         app_label = "mainapp"

#         managed = False
        
        
# class Provision(models.Model):
#     pro_code = CharField(primary_key=True, max_length=20)
#     username = models.ForeignKey(User,
#                                 to_field="username",
#                                 db_column="username",
#                                 on_delete=models.CASCADE)
#     pro_name = CharField(max_length=20)
#     pro_content = CharField(max_length=2000)
#     pro_essential = CharField(max_length=1)
    
    
#     class Meta:
#         db_table = "PROVISION"

#         app_label = "mainapp"

#         managed = False
        
# class Provision_history(models.Model):
#     his_num = IntegerField(primary_key=True)
#     pro_code = models.ForeignKey(Provision,
#                                 to_field="pro_code",
#                                 db_column="pro_code",
#                                 on_delete=models.CASCADE)
#     username = models.ForeignKey(User,
#                                 to_field="username",
#                                 db_column="username",
#                                 on_delete=models.CASCADE)
#     his_consent = CharField(max_length=1)
#     his_date = DateTimeField(auto_now_add = True)
    
#     class Meta:
#         db_table = "PROVISIONHISTORY"

#         app_label = "mainapp"

#         managed = False
        
# class Naver_account(models.Model):
#     naver_id = CharField(primary_key=True, max_length=20)
#     username = models.ForeignKey(User,
#                                 to_field="username",
#                                 db_column="username",
#                                 on_delete=models.PROTECT)
#     naver_token = CharField(max_length=255)
    
#     class Meta:
#         db_table = "NAVER_ACCOUNT"

#         app_label = "mainapp"

#         managed = False

# class google_account(models.Model):
#     google_id = CharField(primary_key=True, max_length=20)
#     username = models.ForeignKey(User,
#                                 to_field="username",
#                                 db_column="username",
#                                 on_delete=models.PROTECT)
#     google_token = CharField(max_length=255)
    
#     class Meta:
#         db_table = "GOOGLE_ACCOUNT"

#         app_label = "mainapp"

#         managed = False

# class Kakao_account(models.Model):
#     kakao_id = CharField(primary_key=True, max_length=20)
#     username = models.ForeignKey(User,
#                                 to_field="username",
#                                 db_column="username",
#                                 on_delete=models.PROTECT)
#     kakao_token = CharField(max_length=255)
    
#     class Meta:
#         db_table = "KAKAO_ACCOUNT"

#         app_label = "mainapp"

#         managed = False

class Category(models.Model):
    cate_num = IntegerField(primary_key=True)
    username = models.ForeignKey(User,
                                to_field="username",
                                db_column="username",
                                on_delete=models.CASCADE)
    cate_name = CharField(max_length=100, unique=True)
    cate_date = DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = "CATEGORY"

        app_label = "mainapp"

        managed = False

class Community(models.Model):
    com_num = AutoField(primary_key=True)
    username = models.ForeignKey("User",
                                to_field="username",
                                db_column="username",
                                on_delete=models.CASCADE)
    cate_name = CharField(max_length=255)
    com_title = CharField(max_length=255)
    com_content = TextField()
    com_combool = CharField(max_length=1)
    com_date = DateTimeField(auto_now_add = True)
    com_count = IntegerField(default=1)
    com_path = CharField(max_length=100)
    
    class Meta:
        db_table = "Community"

        app_label = "mainapp"

        managed = False

class Comment(models.Model):
    comment_num = AutoField(primary_key=True)
    com_num = models.ForeignKey("Community",
                                to_field="com_num",
                                db_column="com_num",
                                on_delete=models.CASCADE)
    username = models.ForeignKey("User",
                                to_field="username",
                                db_column="username",
                                on_delete=models.CASCADE)
    comment_content = TextField()
    comment_create_date = DateTimeField(auto_now_add = True)
    comment_modified_date = DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "COMMENT"

        app_label = "mainapp"

        managed = False
