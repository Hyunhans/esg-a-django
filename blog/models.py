from unittest.util import _MAX_LENGTH
from django.db import models

from django.core.validators import MaxValueValidator

# Create your models here.
class Restaurant(models.Model):
    """맛집"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    average_score = models.PositiveSmallIntegerField(  #양수만 입력할수
        validators = [
            MaxValueValidator(5),  #5이상의 양수를 입력할 수 없다.

        ]
    )

    def get_absolute_url(self):
        # 향후에는 장고의 URL Reverse 기능을 사용하기 .
        return f"/blog/restaurant/{self.pk}/"


class Post(models.Model):  #class 의 첫글짜는 항상 대문자

    title = models.CharField(max_length=30)  #CharField 는 길이 제한이 있는 메소드

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        # 향후에는 장고의 URL Reverse 기능을 사용하기 .
        return f"/blog/{self.pk}/"



    def __str__(self):
        # self.pk : 기본적으로 int 값이다. 
        return f'[{self.pk}] {self.title}'