from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include("users.urls")),
    path('accounts/',include("django.contrib.auth.urls")),
    path('books/',include("book.urls")),

    # RedirectView == redireect()
    path('',RedirectView.as_view(pattern_name="users:home")),
]
