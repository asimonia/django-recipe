from django.db import models



class Meal(models.Model):
	# leave it blank, then it is required.
	# recipe_id will link from bigoven api
	date = models.DateField()
	recipe_id = models.CharField(max_length=100)
	recipe_url = models.URLField()
	recipe_nickname = models.CharField(max_length=100)

	def __str__(self):
		return self.recipe_id
