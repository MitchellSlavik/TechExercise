from django.db import models

class Category(models.Model):
	category = models.CharField(max_length=100)
	short_name = models.CharField(max_length=20)
	def __str__(self):
		return self.category

class Question(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	points = models.IntegerField(default=0)
	category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='questions')

class Answer(models.Model):
	answer = models.TextField()
	points = models.IntegerField(default=0)
	question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')
	
