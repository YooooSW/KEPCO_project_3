# from django.db import models
# # - DB에서 varchar2 또는 char 등 문자열 타입
# from django.db.models.fields import CharField
# # - DB에서 number 또는 integer 등 숫자형 타입
# from django.db.models.fields import IntegerField
# # - DB에서 날짜와 시간을 갖는 필드.
# # 날짜만 가질 경우는 DateField, 시간만 가질 경우는 TimeField를 사용한다.
# from django.db.models.fields import DateTimeField
# # - DB에서 대용량 문자열을 갖는 필드
# from django.db.models.fields import TextField
# # - DB에서 파일 업로드 필드
# # from django.db.models.fields import FileField
# # - DB에서 	FileField의 파생클래스로서 이미지 파일인지 체크
# # from django.db.models.fields import ImageField
# # Create your models here.

# class User(models.Model):
#     user_id = model.CharField(primary_key=True, max_length=20, null=False)
#     user_name = model.CharField(max_length=20, null=False)
#     user_email = model.CharField(max_length=20, null=False)
#     user_pass = model.CharField(max_length=20, null=False)
#     user_phon = model.CharField(max_length=20, null=False)
    
# #     class Meta:
# #         # 실제 사용할 테이블 이름 정의
# #         db_table = "user_"

# #         # 사용할 앱 이름 정의
# #         app_label = "mainapp"

# #         # 외부 데이터베이스에 테이블 존재여부 확인
# #         # - 존재하면 : False
# #         # - 존재하지 않으면 : True
# #         # --> 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
# #         managed = False
        
# class User_img(models.Model):
#     user_num = models.IntegerField(primary_key=True, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     user_path = model.CharField(max_length=100, null=False)
#     user_date = model.DateField(auto_now = True, null=False)
    
# #     class Meta:
# #         db_table = "user_img"

# #         app_label = "mainapp"

# #         managed = False
        
# class User_service(models.Model):
#     user_ser_num = models.IntegerField(primary_key=True, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     user_create = model.DateField(auto_now_add = True, null=False)
#     user_pass_modified = model.DateField(auto_now = True, null=False)
#     user_login_date = model.DateField(auto_now = True, null=False)
#     user_count = models.IntegerField(null=False)
    
# #     class Meta:
# #         db_table = "user_img"

# #         app_label = "mainapp"

# #         managed = False
        
# class Provision(models.Model):
#     pro_code = CharField(primary_key=True, max_length=20, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     pro_name = model.CharField(max_length=20, null=False)
#     pro_content = model.CharField(max_length=2000, null=False)
#     pro_essential = model.CharField(max_length=1, null=False)
    
    
# #     class Meta:
# #         db_table = "provision"

# #         app_label = "mainapp"

# #         managed = False
        
# class Provision_history(models.Model):
#     his_num = models.IntegerField(primary_key=True, null=False)
#     pro_code = models.ForeignKey(Provision,
#                                 to_field="pro_code",
#                                 db_column="pro_code",
#                                 on_delete=models.PROTECT)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     his_consent = model.CharField(max_length=1, null=False)
#     his_date = model.DateField(auto_now_add = True, null=False)
    
# #     class Meta:
# #         db_table = "provisionhistory"

# #         app_label = "mainapp"

# #         managed = False
        
# class Naver_account(models.Model):
#     naver_id = model.CharField(primary_key=True, max_length=20, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     naver_token = model.CharField(max_length=255, null=False)
    
# #     class Meta:
# #         db_table = "naver_account"

# #         app_label = "mainapp"

# #         managed = False

# class google_account(models.Model):
#     google_id = model.CharField(primary_key=True, max_length=20, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     google_token = model.CharField(max_length=255, null=False)
    
# #     class Meta:
# #         db_table = "google_account"

# #         app_label = "mainapp"

# #         managed = False

# class Kakao_account(models.Model):
#     kakao_id = model.CharField(primary_key=True, max_length=20, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     kakao_token = model.CharField(max_length=255, null=False)
    
# #     class Meta:
# #         db_table = "kakao_account"

# #         app_label = "mainapp"

# #         managed = False

# class Category(models.Model):
#     cate_num = models.IntegerField(primary_key=True, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     cate_name = model.CharField(max_length=100, null=False)
#     cate_date = model.DateField(auto_now_add = True, null=False)
    
# #     class Meta:
# #         db_table = "category"

# #         app_label = "mainapp"

# #         managed = False

# class Community(models.Model):
#     com_num = models.IntegerField(primary_key=True, null=False)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     cate_num = models.ForeignKey(Category,
#                                 to_field="cate_num",
#                                 db_column="cate_num",
#                                 on_delete=models.PROTECT)
#     com_title = model.CharField(max_length=255, null=False)
#     com_content = model.TextField(null=False)
#     com_combool = model.models.CharField(max_length=1, null=False)
#     com_date = model.DateField(auto_now_add = True, null=False)
#     com_count = model.IntegerField(null=False)
#     com_path = model.CharField(max_length=100, null=False)
    
# #     class Meta:
# #         db_table = "community"

# #         app_label = "mainapp"

# #         managed = False

# class Comment(models.Model):
#     comment_num = models.IntegerField(primary_key=True, null=False)
#     com_num = models.ForeignKey(Community,
#                                 to_field="com_num",
#                                 db_column="com_num",
#                                 on_delete=models.PROTECT)
#     user_id = models.ForeignKey(User,
#                                 to_field="user_id",
#                                 db_column="user_id",
#                                 on_delete=models.PROTECT)
#     comment_content = model.TextField(null=False)
#     comment_create_date = model.DateField(auto_now_add = True, null=False)
#     comment_modified_date = model.DateField(auto_now = True, null=False)
    
# #     class Meta:
# #         db_table = "comment"

# #         app_label = "mainapp"

# #         managed = False
