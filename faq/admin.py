from django.contrib import admin

from .models import Question, Category, Answer

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)
