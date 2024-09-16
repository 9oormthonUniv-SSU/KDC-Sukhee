from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model): # DB Table for 설문조사 주제
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

class Choice(models.Model): # 주제별 선택지
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #주제 id 값
    choice_text = models.CharField(max_length=200) # 선택지 텍스트
    votes = models.IntegerField(default=0) # 해당 선택지의 득표 수

    def __str__(self):
        return self.choice_text
