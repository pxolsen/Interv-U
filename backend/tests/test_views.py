from django.test import TestCase, Client
from django.urls import reverse
from tests.answers import all_questions
import json

class Test_views(TestCase):

    # Mocking our database using fixtures.
    fixtures = [
        "question_data.json"
    ]

    # Creating a client instance that can be used for every test using self.client.
    def setUp(self):
        client = Client()
    
    def test_get_all_question(self):
        # Client sends a GET request to URL by using the name endpoint.
        # In this case, the 'all_questions' name will ping our answers.py file as the endpoint instead of our actual API.
        # Our answers.py file is being pinged instead of our actual API due to line #3 above.
        response = self.client.get(reverse('all_questions'))
        response_body = json.loads(response.content)
        self.assertEquals(response_body, all_questions)