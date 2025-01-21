from django.shortcuts import render,redirect,get_object_or_404
from ..models import Question
from django.core.paginator import Paginator



def detail(request,id):
    question = get_object_or_404(Question,id=id)

    # is_liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     is_liked = True
    # answer = get_object_or_404(Answer,id=id)

    return render(request,"board/question_detail.html",{"question":question})

def index(request):

    page = request.GET.get("page",1)
    # 검색
    keyword = request.GET.get("keyword","")

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
