from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse
from allauth.account.views import PasswordChangeView

class CustomUserCreationForm(UserCreationForm):

  class Meta:
    model = get_user_model()           # AbstractUser에서 상속받아 커스텀한 User
    fields = ('username',
              'password1',
              'password2',
              'email',
              'phon',
              'nickname')
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('nickname',)
        
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms
from django.contrib.auth.models import User as auth_user
from .models import User

class PasswordResetForm(auth_forms.PasswordResetForm):
    username = auth_forms.UsernameField(label="사용자ID")  # CharField 대신 사용

    # validation 절차:
    # 1. username에 대응하는 User 인스턴스의 존재성 확인
    # 2. username에 대응하는 email과 입력받은 email이 동일한지 확인

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(username=data).exists():
            raise ValidationError("해당 사용자ID가 존재하지 않습니다.")

        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email:
            if User.objects.get(username=username).email != email:
                raise ValidationError("사용자의 이메일 주소가 일치하지 않습니다")

    def get_users(self, email=''):
        active_users = User.objects.filter(**{
            'username__iexact': self.cleaned_data["username"],
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password()
        )
        
from django import forms
from mainapp.models import Community, Comment

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community # 사용할 모델
        fields = ['com_num', 'com_title', 'com_content', 'username', 'cate_name'] # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'com_num' : '게시글번호',
            'com_title' : '제목',
            'com_content' : '내용',
            'username' : '작성자',
            'cate_name' : '카테고리',
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_num',
                  'comment_content',
                  'username',
                  'com_num']
        labels = {
            'comment_num' : '댓글번호',
            'comment_content' : '댓글내용',
            'username' : '작성자',
            'com_num' : '게시글 번호',
        }