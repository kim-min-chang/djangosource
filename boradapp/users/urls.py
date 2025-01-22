from django.urls import path,reverse_lazy
from .views import register
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("register/",register,name="register"),
    path("login/",LoginView.as_view(template_name="users/login.html"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),  
     path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
            success_url=reverse_lazy("home"),
        ),
        name="password_change",
    ),    
    path(
        "password_reset/",
        auth_views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
