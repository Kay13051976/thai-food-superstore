from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Recipes, Category, Comment


# Create your views here.
def all_recipes(request):
    datas = Recipes.objects.order_by('-id')
    if request.user.is_authenticated:

        if request.method == 'GET':
            # allcoments = Recipecommments.objects.all().count()
            # newid=allcoments+1
            if 'comment' in request.GET:
                # form = SubscibersForm(request.POST)
                # recipes_recipecommme=recipes_recipecommments.recipes_id()
                # recipes_recipecommme.save()
                # Recipesnewcom = Recipes.id(request.GET['recipeid'])
                # Recipecommments(request.GET['comment'],str(request.user))
                get_post = Recipes.objects.get(id=request.GET['recipesid'])
                RecipesCommments_new = Comment(name=str(request.user), post_name=get_post, body=request.GET['comment'])
                RecipesCommments_new.save()
            # messages.success(request, 'Subscription Successful')
                return redirect('recipes')

    return render(request, 'recipes/recipes.html', {'datas': datas})


def recipes_detail(request, recipes_id):
    """ A view to show individual product details """

    if request.user.is_authenticated:

        if request.method == 'GET':
            if 'comment' in request.GET:
                get_post = Recipes.objects.get(id=request.GET['recipesid'])
                RecipesCommments_new = Comment(name=str(request.user), post_name=get_post, body=request.GET['comment'])
                RecipesCommments_new.save()
                return redirect("recipes_detail", kwargs={"int": int(recipes_id)})

    recipes = get_object_or_404(Recipes, pk=int(recipes_id))
    context = {
                    'recipes': recipes,
                }
    return render(request, 'recipes/recipes-details.html', context)
