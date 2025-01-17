from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 모델에서 사용할 필드 지정
        # 방법1
        # fields = "__all__"
        # exclude_fields= ["created_at","modified_at"]
        # 방법2
        fields = ["title","content","image"]
