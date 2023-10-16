from django.test import SimpleTestCase, TestCase
# Reverse allows us to ping our URLs by name.
# Resolve gives us information about our URL such as routes, args, views, etc.
from django.urls import reverse, resolve
from question_app.views import All_questions, A_question

# Testing that URLs have the correct route and are utilizing the correct API View.

class TestUrls(TestCase):
    def test_all_questions_url(self):
        # Resolve URL to get all the information about it.
        url = resolve(reverse('all_questions'))
        # Using subtest to run another assertion
        with self.subTest():
            # Check to see if the route of our URL when referenced by name is equal to the correct route.
            self.assertEquals(url.route, 'api/questions/')
        # Check to see if we are getting the right API View when following the URL to the endpoint.
        self.assertTrue(url.func.view_class is All_questions)

    def test_a_question_url(self):
        # Resolve URL to get all the information about it.
        # Enter a "kwarg" for the question_id.
        url = resolve(reverse('a_question', kwargs={"id":1}))
        # print(url)
        with self.subTest():
            self.assertEquals(url.route, 'api/questions/<int:id>/')
        self.assertTrue(url.func.view_class is A_question)
        