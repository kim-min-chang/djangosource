from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include("users.urls")),
    # RedirectView == redireect()
    path('',RedirectView.as_view(pattern_name="home")),
]
