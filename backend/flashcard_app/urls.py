from django.urls import path
from .views import All_flashcards, A_flashcard

urlpatterns = [
    path("", All_flashcards.as_view(), name='all_flashcards'),
    # path("create/", Create_flashcard.as_view(), name='create_flashcard'),
    path("<int:flashcard_id>/", A_flashcard.as_view(), name="a_flashcard"),
]