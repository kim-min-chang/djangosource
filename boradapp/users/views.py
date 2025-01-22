from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import UserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
from django.contrib import messages

class CustomPasswordResetView(PasswordResetView):
    template_name = "users/password_reset_form.html"
    success_url = reverse_lazy("users:password_reset_done")

    # 
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            messages.info(self.request,"입력하신 이메일을 확인해 주세요")
        return redirect("users:password_reset")
    



def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
        # db정보와 일치하다면 인증받은 객체 user 리턴
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request, user)

            return redirect("board:index")  
    else:
        form = UserForm()

    return render(request,"users/register.html",{"form":form})

