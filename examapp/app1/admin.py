from django.contrib import admin
from .models import Person, Post

# admin 사이트에서 관리할 모델 등록
# 1) admin.site.register(모델명) - 세부지정 불가
admin.site.register(Person)

# 2)
# class PostAdmin(admin.ModelAdmin):
#     """
#     세부지정
#     """
#     pass
# admin.site.register(Post)

# 3) 2)번 개선
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # __str__ 기준으로 admin 페이지에서 보여지는 게 기본
    # list_display 지정하면 __str__ 은 무시된다.
    list_display = ("title","author_name","is_published","created_at")
    # 조회할때 상세보기 링크의 위치를 바꾼다
    list_display_links = ("author_name",)
    search_fields =("title",)
