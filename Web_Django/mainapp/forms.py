from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

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