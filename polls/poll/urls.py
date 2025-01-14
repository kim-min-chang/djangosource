from django.urls import path
from . import views

app_name= "poll"

# path("경로", 뷰 , name="명칭")
# 뷰 - 1) 함수형 뷰 2) 클래스 뷰

urlpatterns = [
    # http://127.0.0.1/polls/
    path("",views.index,name="index"),
    # http://127.0.0.1/pools/1 : 1번질문 조회
    path("<int:question_id>/",views.detail,name="detail"),
    # http://127.0.0.1/pools/1/vote : 1번 질문에 대한 답변 선택
    path("<int:question_id>/vote/",views.vote,name="vote"),
    # http://127.0.0.1/pools/1/results : 투표결과보기
    path("<int:question_id>/results/",views.results,name="results"),
]

