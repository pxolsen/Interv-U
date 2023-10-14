from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from client_app.views import User_permissions
from flashcard_app.serializers import FlashCard, FlashCardSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class All_flashcards(User_permissions):
    def get(self, request):
        flashcards = FlashCardSerializer(request.user.flashcards.all(), many=True)
        return Response(flashcards.data)

class Create_flashcard(User_permissions):
    def post(self, request):
        user = request.user
        question = request.data["question"]
        new_flashcard = FlashCardSerializer(FlashCard(user=user, question=question))
        new_flashcard.save()
        return Response(new_flashcard.data, status=HTTP_201_CREATED)

class Update_flashcard(User_permissions):
    pass


