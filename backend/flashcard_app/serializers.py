from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import FlashCard
from client_app.models import Client
from question_app.models import Question

class FlashCardSerializer(ModelSerializer):
    client_id = PrimaryKeyRelatedField(queryset=Client.objects.all())
    question_id = PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = FlashCard
        fields = ['id', 'client', 'question', 'answer', 'favorite', 'asked_in_interview', 'forget']