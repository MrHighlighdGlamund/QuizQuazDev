from django.contrib import admin

# Register your models here.
from .models import QuizLibary
from .models import Question

admin.site.register(QuizLibary)
admin.site.register(Question)
