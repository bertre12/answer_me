from django.contrib import admin

from .models import Question, Choice

# Настройка отображения административной панели.
admin.site.site_header = 'Администратор'
admin.site.site_title = 'Админ-панель'
admin.site.index_title = 'Административная зона'


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ["question_text"]}), ('Дата добавления', {
        "fields": ["pub_date"], "classes": ["collapse"]}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
