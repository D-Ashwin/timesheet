from django.db import models

# Create your models here.
class Userdetails(models.Model):
	# user=models.
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	gender=models.CharField(max_length=10)
	designation=models.CharField(max_length=255)
	mobile=models.BigIntegerField()
	dob=models.DateField(auto_now=False)
	is_deleted=models.BooleanField(default=False)
	created_at=models.DateField(auto_now=False)
	updated_at=models.DateField(auto_now=False)

	def __str__(self):
		return self.first_name