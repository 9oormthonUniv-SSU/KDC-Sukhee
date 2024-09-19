from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    # Question 추가 페이지 내 항목들의 순서 변경(지정)
    fields = ['pub_date', 'question_text'] # fields 변수명은 고정입니다.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
