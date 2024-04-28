from django.shortcuts import render, redirect, reverse, get_object_or_404
from . models import RecipeCommments
# Create your views here.


def index(request):
    """ A view to return the index page """
# comment
    RecipeComm = RecipeCommments.objects.all().order_by('-id')
    if request.user.is_authenticated:

        if request.method == 'GET':
            allcoments = RecipeCommments.objects.all().count()
            newid = allcoments+1
            if 'comment' in request.GET:
                # form = SubscibersForm(request.POST)
                RecipeCommments_new = RecipeCommments(
                    newid, request.GET['recipeid'], str(request.user), request.GET['comment'])
                RecipeCommments_new.save()
            # messages.success(request, 'Subscription Successful')
                return redirect('home')

    context = {
        'RecipeCommments': RecipeComm,
    }

    return render(request, 'home/index.html', context)
