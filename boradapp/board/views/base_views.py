from django.shortcuts import render,redirect,get_object_or_404
from ..models import Question ,QuestionCount
from django.core.paginator import Paginator
from django.db.models import Q,Count
from tools.utils import get_client_ip


def detail(request,id):
    question = get_object_or_404(Question,id=id)

    page = request.GET.get("page",1)
    # 검색
    keyword = request.GET.get("keyword","")

    so = request.GET.get("so","")

    ip = get_client_ip()
    cnt = QuestionCount.objects.filter(ip=ip,question=question)

    if cnt == 0:
        qc = QuestionCount(ip=ip,question=question)
        qc.save()
        if question.view_cnt:
            question.view_cnt =+1
        else:
            question.view_cnt =1
        question.save()

    context = {
        "question":question,
        "page":page,
        "keyword":keyword,
        "so":so,
    }
    return render(request, "board/question_detail.html", context)

    # is_liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     is_liked = True
    # answer = get_object_or_404(Answer,id=id)
    

def index(request):

    page = request.GET.get("page",1)
    # 검색
    keyword = request.GET.get("keyword","")

    so = request.GET.get("so","")

    objects = Question.objects.order_by("-created_at")

    if so== "popular":
        objects = Question.objects.annotate(num_voter= Count('voter')).order_by("-num_voter","-created_at")
    elif so== "recommend":
        objects = Question.objects.annotate(num_answer=Count('answer')).order_by("-num_answer","-created_at")
    else:
        objects = Question.objects.order_by("-created_at")


    # 검색어가 제목 or 내용 or질문 작성자 or 답변 작성자에 포함된 경우
    if keyword:
        objects = objects.filter().distinct(
            Q(subject__icontains=keyword)
            |Q(content__icontains=keyword)
            |Q(author__icontains=keyword)
            |Q(answer__author__username__icontains=keyword)
        ).distinct()



    
    paginator = Paginator(objects, 10)

    question_list = paginator.get_page(page)
     
    context = {"question_list":question_list, "page":page,"keyword":keyword}
    return render(request, "board/question_list.html",{"context":context})
