from django.db import models

class Question(models.Model): # DB Table for 설문조사 주제
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model): # 주제별 선택지
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #주제 id 값
    choice_text = models.CharField(max_length=200) # 선택지 텍스트
    votes = models.IntegerField(default=0) # 해당 선택지의 득표 수
