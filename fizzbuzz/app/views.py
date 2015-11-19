from django.shortcuts import get_object_or_404
from .models import FizzBuzz
from .serializers import FizzBuzzSerializer
from rest_framework import status, viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class FizzBuzzViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	permission_classes = (AllowAny,)
	queryset = FizzBuzz.objects.all()
	serializer_class = FizzBuzzSerializer
		
	def create(self, request):
		fizzbuzz = request.data
		fizzbuzz['useragent']=request.META['HTTP_USER_AGENT']

		serializer = FizzBuzzSerializer(data=fizzbuzz)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
