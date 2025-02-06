import os
import django
from scrape.scraper import scrape
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from detection.models import Recipe, Ingredient

with open('url.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    urls = [row['URL'] for row in reader]

for url in urls:
    recipe_data = scrape(url)

    recipe = Recipe.objects.create(
        title =             recipe_data['title'],
        rating =            recipe_data['rating'],
        servings =          recipe_data['servings'],
        time_hour =         recipe_data['time_h'],
        time_minute =       recipe_data['time_m'],
        ingredient_name =   recipe_data['ingredient_name'],
        ingredient_amount = recipe_data['ingredient_amount'],
        ingredient_unit =   recipe_data['ingredient_unit'],
        instructions =      recipe_data['instructions']
    )

    existing_ingredients = Ingredient.objects.filter(name__in=recipe_data['ingredient_name'])
    
    recipe.ingredients.add(*existing_ingredients)

    recipe.save()
    print(recipe_data['title'] + ' was added')