from django.shortcuts import render

# Create your views here.


def all_recipes(request, recipes_id):
    """ A view to show individual recipes details """

    return render(request, 'recipes/recipes.html')
