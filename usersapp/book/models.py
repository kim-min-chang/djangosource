from django.db import models

class Book(models.Model):
    """
    code(숫자),title,author,price(숫자),created_at
    """
    code = models.IntegerField(verbose_name="도서코드",unique=True)
    title = models.CharField(max_length=200,verbose_name="도서명")
    author = models.CharField(max_length=100,verbose_name="저자")
    price = models.IntegerField(verbose_name="도서가격")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="등록일시")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "booktbl"