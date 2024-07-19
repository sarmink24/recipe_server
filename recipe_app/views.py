# from django.shortcuts import render

# Create your views here.

# recipe_app/views.py
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views import View
from django.conf import settings
import os

def home(request):
    return HttpResponse("Welcome to the Django API!")

class RecipeListView(View):
    def get(self, request):
        data_file_path = os.path.join(settings.BASE_DIR, 'recipe_app', 'data.json')
        with open(data_file_path, 'r') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)

class RecipeDetailView(View):
    def get(self, request, recipe_id):
        data_file_path = os.path.join(settings.BASE_DIR, 'recipe_app', 'data.json')
        with open(data_file_path, 'r') as file:
            data = json.load(file)
        recipe = next((item for item in data if item['id'] == recipe_id), None)
        if recipe:
            return JsonResponse(recipe, safe=False)
        return JsonResponse({'error': 'Recipe not found'}, status=404)
