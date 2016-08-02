from rest_framework import serializers
from recipe_list.models import Meal


class MealSerializer(serializers.ModelSerializer):


	class Meta:
		model = Meal
		fields = ('id', 'date', 'recipe_id', 'recipe_url', 'recipe_nickname')