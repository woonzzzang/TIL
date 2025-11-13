# 인증 부분 공부한지 오래됐으니까.. 
# 강사님이 문제를 낸다면!

# 1. login 동작이 안 되는 경우

path('<username>', views.profile)
path('login',views.login)

# 2. UserCreationForm / UserChangeForm 이 아닌 CustomUserCreationForm / CustomUserChangeForm 을 사용하는 이유

# 3. 파라미터의 차이점

form = AuthenticationForm(request, request.POST)
form = AuthenticationForm()

form = CustomUserCreationFrom(request.POST)
form = CustomUserCreationForm()

form = CustomUserChangeForm(request.POST, instance=request.user)
form = CustomUserChangeForm(instance=request.user)

form = PasswordChangeForm(request.user, request.POST)

# 4. auth_login을 안 쓰면?

from django.contrib.auth import login
login(request, form.get_user())

from django.contrib.auth import login as auth_login
auth_login(request, form.get_user())

# 5. @login_required

# 6. 적용하는 파일에 따라

User = get_user_model()
User = settings.AUTH_USER_MODEL # models.py 에서