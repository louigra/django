from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.username    

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    created_by = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_text = models.CharField(max_length=200) #required
    ingredient_amount = models.CharField(max_length=200, blank=True, null=True) #optional
    ingredient_unit = models.CharField(max_length=200, blank=True, null=True) #optional
    def __str__(self):
        return self.ingredient_text
    
class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    instruction_text = models.CharField(max_length=500)
    instruction_order = models.IntegerField(default=0)
    def __str__(self):
        return self.instruction_text