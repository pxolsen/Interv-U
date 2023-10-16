from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from client_app.views import User_permissions
from flashcard_app.serializers import FlashCard, FlashCardSerializer
from question_app.models import Question
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class All_flashcards(User_permissions):
    def get(self, request):
        flashcards = FlashCardSerializer(request.user.flashcards.all(), many=True)
        return Response(flashcards.data)
    
    def post(self, request):
        client = request.user
        question_id = request.data.get("question")
        question = Question.objects.get(id=question_id)
        new_flashcard = FlashCard(client=client, question=question)
        new_flashcard.save()
        return Response(FlashCardSerializer(new_flashcard).data, status=HTTP_201_CREATED)

class A_flashcard(User_permissions):
    def get(self, request, flashcard_id):
        flashcard = request.user.flashcards.get(id=flashcard_id)
        return Response(FlashCardSerializer(flashcard).data)
    
    def put(self, request, flashcard_id):
        flashcard = request.user.flashcards.get(id=flashcard_id)
        flashcard.answer = request.data.get("answer")
        flashcard.favorite = request.data.get("favorite")
        flashcard.asked_in_interview = request.data.get("asked_in_interview")
        flashcard.forget = request.data.get("forget")
        return Response(FlashCardSerializer(flashcard).data)


