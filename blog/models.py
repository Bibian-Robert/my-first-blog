from django.db import models
from django.utils import timezone
# Create your models here.
#This is an object called post containing object properties and actions
class Post(models.Model):
	#defining each type of field
	author=models.ForeignKey('auth.User', on_delete=models.PROTECT)#link to another model
	text=models.CharField(max_length=200)
	title=models.TextField()
	created_date=models.DateTimeField(default
		=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date=timezone.now
		self.save()

	def __str__(self):
		return self.title

