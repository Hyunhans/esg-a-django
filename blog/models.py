from django.db import models

# Create your models here.

class Post(models.Model):  #class 의 첫글짜는 항상 대문자

    title = models.CharField(max_length=30)  #CharField 는 길이 제한이 있는 메소드

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        # self.pk : 기본적으로 int 값이다. 
        return f'[{self.pk}] {self.title}'