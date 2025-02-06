from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField( max_length=100, unique=True)
    rating = models.CharField( max_length=15, blank=True )
    servings = models.CharField( max_length=15, blank=True )
    time_hour = models.CharField( max_length = 15, blank=True )
    time_minute = models.CharField( max_length = 15, blank=True )
    ingredients = models.ManyToManyField( Ingredient, related_name= 'search_recipes')
    ingredient_name = ArrayField(
        models.CharField( max_length=50 ),
        blank=False,
        default=list
    )
    ingredient_amount = ArrayField(
        models.CharField( max_length=10 ),
        blank=True,
        default=list
    )
    ingredient_unit = ArrayField(
        models.CharField( max_length=20 ),
        blank=True,
        default=list
    )
    instructions = ArrayField(
        models.TextField(),
        blank=True,
        default=list
    )

    def __str__(self):
        return self.title


# from detection.models import Ingredient
# ingredients_list = ['apple', 'background', 'beef', 'cabbage', 'carrot', 'chicken', 'chicken_broth', 'chili', 'cilantro', 'coriander', 'cucumber', 'egg', 'fish', 'garlic', 'ginger', 'honey', 'lemon', 'lime', 'milk', 'mushroom', 'noodle', 'olive', 'onion', 'orange', 'parsley', 'peanut', 'pork', 'potato', 'rice', 'salmon', 'scallion', 'shrimp', 'stock', 'tomato', 'yoghurt']
# ingredient_objs = [Ingredient(name=i_name) for i_name in ingredients_list]
# Ingredient.objects.bulk_create(ingredient_objs, ignore_conflicts = True)