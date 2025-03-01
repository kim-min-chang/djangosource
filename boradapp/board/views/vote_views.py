from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from board.models import Question,Answer
from django.contrib import messages

@login_required(login_url="users:login")
def vote_question(request, id):
    # 질문추천
    question = get_object_or_404(Question,id=id)
    # 자신이 작성한 글은 추천에서 제외
    if request.user == question.author:
        messages.warning(request,"본인이 작성한 글은 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)
    return redirect("board:detail",id)

@login_required(login_url="users:login")
def vote_answer(request,id):
    # 답변추천
    answer = get_object_or_404(Answer,id=id)
    # 자신이 작성한 글은 추천에서 제외
    if request.user == answer.author:
        messages.warning(request,"본인이 작성한 글은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)
    return redirect("board:detail",answer.Question.id)