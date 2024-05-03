from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Recepies, Category, Comment


# Create your views here.
def all_recepies(request):
    datas = Recepies.objects.order_by('-id')
    if request.user.is_authenticated:

        if request.method == 'GET':
            # allcoments = Recipecommments.objects.all().count()
            # newid=allcoments+1
            if 'comment' in request.GET:
                # form = SubscibersForm(request.POST)
                # recepies_recipecommme=recepies_recipecommments.recepies_id()
                # recepies_recipecommme.save()
                # Recepiesnewcom = Recepies.id(request.GET['recipeid'])
                # Recipecommments(request.GET['comment'],str(request.user))
                get_post = Recepies.objects.get(id=request.GET['recipeid'])
                RecipeCommments_new = Comment(name=str(request.user), post_name=get_post, body=request.GET['comment'])
                RecipeCommments_new.save()
            # messages.success(request, 'Subscription Successful')
                return redirect('recepies')

    return render(request, 'recepies/recepies.html', {'datas': datas})


def recepies_detail(request, recepies_id):
    """ A view to show individual product details """
    receipe = get_object_or_404(Recepies, pk=recepies_id)
    if request.user.is_authenticated:

        if request.method == 'GET':
            if 'comment' in request.GET:
                get_post = Recepies.objects.get(id=request.GET['recipeid'])
                RecipeCommments_new = Comment(name=str(request.user), post_name=get_post, body=request.GET['comment'])
                RecipeCommments_new.save()

    return redirect("recepies_detail", kwargs={"int": int(recepies_id)})

    context = {
        'recipe': receipe,
    }

    return render(request, 'recepies/recepies-details.html', context)
