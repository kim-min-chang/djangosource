from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # 비밀번호 변경 
    # path(
    #     "password_change/", auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"), name="password_change"
    # ),
    # path(
    #     "password_change/done/",
    #     auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change.done.html"),
    #     name="password_change_done",
    # ),
    # 비밀번호 변경시 템플릿 변경 +이동하는 경로 변경
    # 비밀번호 변경 => 세션제거 => 재로그인: 장고는 이부분을 스스로 처리해줌
    path(
        "password_change/",auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
            success_url=reverse_lazy("home"),
        ),
        name="password_change"
    ),
    # 비밀번호 초기화
    #  path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/",views.CustomPasswordResetView.as_view(),name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("register/",views.users_register,name="register"),


]