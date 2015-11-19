from rest_framework import serializers
from .models import FizzBuzz

class FizzBuzzSerializer(serializers.ModelSerializer):
	class Meta:
		model = FizzBuzz
		field = ('fizzbuzz_id', 'creation_date', 'useragent', 'message')