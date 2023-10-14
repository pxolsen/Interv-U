from django.urls import path
from .views import All_flashcards, Create_flashcard, Update_flashcard

urlpatterns = [
    path("", All_flashcards.as_view(), name='all_flashcards'),
    path("create/", Create_flashcard.as_view(), name='create_flashcard'),
    path("update/", Update_flashcard.as_view(), name="update_flashcard"),
]