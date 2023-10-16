from django.test import TestCase
from django.core.exceptions import ValidationError
from client_app.models import Client
from question_app.models import Question
from flashcard_app.models import FlashCard

# Setting global email variable for reference in tests.
email="email@gmail.com"

class client_test(TestCase):
    def test_01_create_client_instance(self):
        # Manually set username to email. When API pinged, our views will automatically make username = email.
        new_client = Client(email=email, username=email, first_name="First", last_name="Last", password="123")
        try:
            # Running full clean to run validators on this new client instance
            new_client.full_clean()
            # Checking to see if the instance was created
            self.assertIsNotNone(new_client)
        except ValidationError as e:
            # print(e.message_dict)
            self.fail()

    def test_02_create_client_with_improper_first_name(self):
        new_client = Client(email=email, username=email, first_name="F!rst", last_name="Last", password="123")
        try:
            # Running full clean to run validators on this new client instance
            new_client.full_clean()
            # If the test gets through full_clean, our name validator did not work properly. The test will fail below.
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assertTrue('Improper name format' in e.message_dict['first_name'])
    
    def test_03_create_client_with_improper_email_format(self):
        try:
            new_client = Client(email="email@email", username="email@email", first_name="First", last_name="Last", password="123")
            # Running full clean to run validators on this new client instance
            new_client.full_clean()
            # If the test gets through full_clean, our name validator did not work properly. The test will fail below.
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assertTrue('Enter a valid email address.' in e.message_dict['email'])

class flashcard_test(TestCase):
    def test_04_create_flashcard_instance(self):
        try: 
            new_client = Client(email=email, username=email, first_name="First", last_name="Last", password="123")
            new_client.save()
            new_question = Question(text="Will this test pass?")
            new_question.save()
            new_flashcard = FlashCard(client=new_client, question=new_question)
            new_flashcard.full_clean()
            self.assertIsNotNone(new_flashcard)
        except ValidationError as e:
            # print(e.message_dict)
            self.fail()
