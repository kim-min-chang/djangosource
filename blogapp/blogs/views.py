from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required : 로그인이 안되어 있을 때 로그인 페이지로 이동

@login_required(login_url="/users/login")
def comment_create(request,pk):
    if request.method == "POST":
        content = request.POST.get("content").strip()
        post_pk = request.POST.get("post_pk").strip()

        post = get_object_or_404(Post, pk=pk)

        if content:
            # Comment 생성
            # comment = Comment(post=post_pk,user=request.user,content=content)
            # comment.save()
            comment = Comment.objects.create(post=post_pk,user=request.user,content=content)
            return redirect("blogs:detail",pk=comment.post.pk)
        
    messages.error(request,"댓글을 입력해 주세요")
    return redirect("blogs:detail",pk=post_pk)

@login_required(login_url="/users/login")
def blogs_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect("blogs:list")

@login_required(login_url="/users/login")
def blogs_update(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect("blogs:detail",pk=pk)
    else:
        form = PostForm(instance=post)

    return render(request,"blogs/update.html",{"form":form,"pk":pk})

@login_required(login_url="/users/login")
def blogs_create(request):
    if request.method =="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 작성자(==로그인 사용자)
            post.user = request.user
            post.save()
            return redirect("blogs:list")
    else:
        form = PostForm()

    return render(request, "blogs/create.html",{"form":form})

def blogs_list(request):

    # 작성일자 내림차순
    post_list = Post.objects.order_by("-created_at")

    return render(request, "blogs/list.html", {"post_list": post_list})

def blogs_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, "blogs/detail.html",{"post":post})
