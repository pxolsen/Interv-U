from django.contrib import admin
from .models import Client
from question_app.models import Question
from flashcard_app.models import FlashCard

admin.site.register(Client)
admin.site.register(Question)
admin.site.register(FlashCard)
