from django.urls import path
from .views import All_questions, A_question

urlpatterns = [
    path("", All_questions.as_view(), name='all_questions'),
    path("<int:id>/", A_question.as_view(), name='a_question')
]