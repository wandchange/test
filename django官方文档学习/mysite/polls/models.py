# from datetime import timezone, datetime
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        print('self.pub_date : ',self.pub_date,'timezone.now(): ',timezone.now(),'now - datetime.timedelta(days=1): ',now - datetime.timedelta(days=1))
        return now - datetime.timedelta(days=1) <=  self.pub_date <= now #意思是现在的时间减去一天小于或等于发布时间或现在的时间返回True，减去一天代表是最近发布的
        # 没写出具体运算符都是默认以and连接
        # 例： now - datetime.timedelta(days=1) <= self.pub_date and self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text