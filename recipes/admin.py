from django.contrib import admin

# Register your models here.

from .models import Category, Recipes

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    ...
                   

admin.site.register(Category, CategoryAdmin)

# ou 
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     ...
