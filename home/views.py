from django.shortcuts import render, redirect, reverse, get_object_or_404
from . models import RecipesComments
# Create your views here.


def index(request):
    """ A view to return the index page """
# comment
    RecipesComm = RecipesComments.objects.all().order_by('-id')
    if request.user.is_authenticated:

        if request.method == 'GET':
            allcoments = RecipesComments.objects.all().count()
            newid = allcoments+1
            if 'comment' in request.GET:
                # form = SubscibersForm(request.POST)
                RecipesComments_new = RecipesComments(
                    newid, request.GET['recipesid'], str(request.user), request.GET['comment'])
                RecipesComments_new.save()
            # messages.success(request, 'Subscription Successful')
                return redirect('home')

    context = {
        'RecipesComments': RecipesComm,
    }

    return render(request, 'home/index.html', context)
