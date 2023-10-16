from django.db import models 
from question_app.models import Question
from client_app.models import Client

class FlashCard(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="flashcards")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="flashcards")
    answer = models.CharField(null=True, blank=True)
    favorite = models.BooleanField(default=False)
    asked_in_interview = models.BooleanField(default=False)
    forget = models.BooleanField(default=False)