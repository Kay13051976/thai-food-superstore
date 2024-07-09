from django.shortcuts import render, redirect, reverse, get_object_or_404
from . models import RecipesCommments
# Create your views here.


def index(request):
    """ A view to return the index page """
# comment
    RecipesComm = RecipesCommments.objects.all().order_by('-id')
    if request.user.is_authenticated:

        if request.method == 'GET':
            allcoments = RecipesCommments.objects.all().count()
            newid = allcoments+1
            if 'comment' in request.GET:
                # form = SubscibersForm(request.POST)
                RecipesCommments_new = RecipesCommments(
                    newid, request.GET['recipesid'], str(request.user), request.GET['comment'])
                RecipesCommments_new.save()
            # messages.success(request, 'Subscription Successful')
                return redirect('home')

    context = {
        'RecipesCommments': RecipesComm,
    }

    return render(request, 'home/index.html', context)
