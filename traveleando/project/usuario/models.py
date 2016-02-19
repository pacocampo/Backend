from django.db import models
from django.contrib.auth.models import User
from category.models import *
# Create your models here.
class MyUser(models.Model):
	#Relations
	user = models.ForeignKey(User)
	perfil = models.ForeignKey(Category)

	#Attributes
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.user.first_name + " " + self.user.last_name)

