from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import FlashCard
from client_app.serializers import Client, ClientSerializer
from question_app.serializers import Question, QuestionSerializer

class FlashCardSerializer(ModelSerializer):
    # client = PrimaryKeyRelatedField(queryset=Client.objects.all())
    # question = PrimaryKeyRelatedField(queryset=Question.objects.all())
    client = ClientSerializer()
    question = QuestionSerializer()

    class Meta:
        model = FlashCard
        fields = ['id', 'client', 'question', 'answer', 'favorite', 'asked_in_interview', 'forget']