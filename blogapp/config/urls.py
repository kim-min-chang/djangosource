from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import blogs_list
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/',include("blogs.urls")),
    path('users/',include("users.urls")),
    # http://127.0.0.1:8000/ => http://127.0.0.1:8000/blogs 요청과 동일한 페이지 보여주기
    # 방법1) blogs 의 views 연결하기
    # path('',blogs_list,name="home"),
    # 방법2) RedirectView 사용하기
    path('',RedirectView.as_view(pattern_name="blogs:list"),name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)