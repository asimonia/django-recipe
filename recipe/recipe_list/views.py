from django.shortcuts import render
from recipe_list.models import Meal
from recipe_list.serializers import MealSerializer
from rest_framework import mixins, generics


# Mixins have the CRUD functionality
# Two class based views
# Collection and Member

class MealList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

	queryset = Meal.objects.all()
	serializer_class = MealSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)