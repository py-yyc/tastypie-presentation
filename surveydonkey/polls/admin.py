from django.contrib import admin
from .models import Choice, Question


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('description', 'question', 'votes')


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'pub_date')
    inlines = [ChoiceInline]


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
