from django.db import models

class FizzBuzz(models.Model):
	fizzbuzz_id = models.AutoField(primary_key=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	useragent = models.CharField(max_length=200)
	message = models.TextField()
		
