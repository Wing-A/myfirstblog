# from django.db import models
# from django.utils import timezone

# # Create your models here.

# class Post(models.Model):
#     #models.Foreignkey 다른 모델에 대한 링크를 의미
#     author = models.ForeignKey('ayth.User')
#     #models.CharField는 글자 수가 제한된 text. 글제목같이 짧은 문자열
#     title = models.CharField(max_length=200)
#     #models.TextField 글자 수에 제한이 없는 긴 text.
#     text = models.TextField()
#     #models.DateTimeField 날짜와 시간을 의미
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = =models.DateTimeField(black=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title