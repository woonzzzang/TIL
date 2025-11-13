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

# 7. person의 차이점
<h1> {{ person.username }}님의 프로필</h1>
<h1> {{ request.user.username }}님의 프로필</h1>

# 8. 로그인 한 사용자와 아닌 경우 분리
{% if request.user.is_authenticated %}
..
{% else %}
..
{% endif %}

# 9. 로그인 한 사용자가 쓴 글만 보이도록
{% for article in articles %}
    {% if request.user == article.user %}

# 10. related name 정의 확인
request.user in article.like_users.all
article in request.user.like_articles.all

# 11. symetrical True/False, 'self'의미
followings = models.ManyToManyField(
    'self', symmetrical=False, related_name='followers'
)

# 12. 역참조가 두 개 일 때 오류 수정: related_name