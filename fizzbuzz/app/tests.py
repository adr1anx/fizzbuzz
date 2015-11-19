from django.test import TestCase
from rest_framework.test import APIClient
from .models import FizzBuzz

class FizzBuzzTest(TestCase):
	def setUp(self):
		self.client = APIClient(HTTP_USER_AGENT='TestAgent/1.0')
		
	def test_save_useragent(self):
		'''
		The only non default behavior to test is automatically setting the useragent
		'''
		self.client.post('/fizzbuzz/', {'message': 'testing!'}, format='json')
		
		self.assertEqual(1, FizzBuzz.objects.count())
		self.assertEqual('TestAgent/1.0', FizzBuzz.objects.all()[0].useragent)