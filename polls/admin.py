from django.contrib import admin
from .models import Question, Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # ('field 집합의 소제목', {'fields': ['field 이름 1', 'field 이름 2', ...]}),
        ("Question title", {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] #  필터 기능
    search_fields = ['question_text'] # 검색 기능

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
