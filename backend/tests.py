from django.test import TestCase
from django.core.exceptions import ValidationError
from client_app.models import Client
from flashcard_app.models import FlashCard
from question_app.models import Question

email = "email@gmail.com"
first_name = "First"
last_name = "Last"
username = email

class client_test(TestCase):

    def test_01_create_client_instance(self):
        new_client = Client(username=email, email=email, first_name=first_name, last_name=last_name)
        try:
            new_client.set_password("123")
            # Running full_clean to run all validators
            new_client.full_clean()
            # Ensuring the instance was actually created
            self.assertIsNotNone(new_client)
        except ValidationError as e:
            print(e.message_dict)
            # If it sends an error the test will fail
            self.fail()

    def test_02_create_client_with_improper_first_name_format(self):
        new_client = Client(email=email, first_name="123!!", last_name=last_name)
        try:
            new_client.set_password("123")
            new_client.full_clean()
            # If the instance runs through full clean and doesn't throw an error, we will fail the test
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            # Checking to make sure we are getting the right error message
            self.assertTrue('Improper name format' in e.message_dict['first_name'])

    def test_03_create_question_instance(self):
        new_question = Question(text="What is the question?")
        try:
            new_question.full_clean()
            self.assertIsNotNone(new_question)
        except ValidationError as e:
            print(e.message_dict)
            self.fail()
        
    def test_04_create_flashcard_instance(self):
        new_client = Client(email="email@gmail.com", first_name="First", last_name="Last")
        new_client.set_password("123")
        new_client.save()
        new_question = Question(text="What is the question?")
        client = Client.objects.get(email="email@gmail.com")
        new_question.save()
        question = Question.objects.get(text="What is the question?")
        new_flashcard = FlashCard(client=client, question=question)
        try:
            new_flashcard.full_clean()
            # print(new_flashcard.client.email)
            # print(new_flashcard.question.text)
            self.assertIsNotNone(new_flashcard)
        except ValidationError as e:
            print(e.message_dict)
            self.fail()