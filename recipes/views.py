from django.shortcuts import render, get_list_or_404, get_object_or_404

from utils.recipes.factory import make_recipe
from .models import Recipes
from django.http import HttpResponse, Http404

# Create your views here.
def Home(request):

    recipes = Recipes.objects.filter(is_published=True).order_by('id')
    # recipes = get_list_or_404(Recipes.objects.filter(is_published=True).order_by('id'))

    context = {
        #  'recipes': [make_recipe() for _ in range(10)] # Passando o range para o template
        'recipes': recipes
    }
    
    return render(request, 'recipes/pages/home.html', context )


def recipe(request, id):
    print(id)
    # recipe = Recipes.objects.get(id=id, is_published=True)
    recipe = get_object_or_404(Recipes, id=id, is_published=True)
    context = {
        'recipe': recipe,
        # 'recipe': make_recipe(),  # Passando o range para o template
        'is_detail_page': True,
                'title': f'{recipe.title}'

    }
    print(recipe )
    
    return render(request, 'recipes/pages/recipe-view.html', context )



def category(request, category_id):

    # recipes = Recipes.objects.filter(category__id=category_id, is_published=True).order_by('id')
    # if not recipes: 
    #     # return HttpResponse(content='Not Found', status=404)
    #     raise Http404('Category not found!')

    recipes = get_list_or_404(Recipes.objects.filter(category__id=category_id, is_published=True).order_by('id'))

    context = {
        #  'recipes': [make_recipe() for _ in range(10)] # Passando o range para o template
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category'
    }
    
    return render(request, 'recipes/pages/category.html', context )
