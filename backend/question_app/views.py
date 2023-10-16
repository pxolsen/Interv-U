from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

class All_questions(APIView):
    def get(self, request):
        questions = QuestionSerializer(Question.objects.all(), many=True)
        return Response(questions.data, status=HTTP_200_OK)
    
class A_question(APIView):
    def get(self, request, id):
        question = QuestionSerializer(Question.objects.get(id=id))
        return Response(question.data, status=HTTP_200_OK)