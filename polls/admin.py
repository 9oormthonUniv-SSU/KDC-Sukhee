from django.contrib import admin
from .models import Question, Choice
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # ('field 집합의 소제목', {'fields': ['field 이름 1', 'field 이름 2', ...]}),
        ("Question title", {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
