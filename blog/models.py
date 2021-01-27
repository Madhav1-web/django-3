from django.db import models

class blogs(models.Model):
	title = models.CharField(max_length=101)
	description = models.TextField(max_length=400)
	date=models.DateField()

	#this shows the name of the title in the admin page itself instead of the default blog object(1,2,3,4)
	def __str__(self):
		return self.title
