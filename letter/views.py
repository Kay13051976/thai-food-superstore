from django.shortcuts import render, redirect , reverse, get_object_or_404
from . models import Subscribers, MailMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.db.models.functions import Lower
# Create your views here.
import pandas as pd

def index(request):
    if request.method == 'GET':
        allsubs = Subscribers.objects.all().count()
        newid=allsubs+1
        if 'subscribemail' in request.GET:
            #form = SubscibersForm(request.POST)
            subscrivers_new=Subscribers(newid,request.GET['subscribemail'])
            subscrivers_new.save()
            messages.success(request, 'Subscription Successful')
            return redirect('letter-index')

    context = {
        'Subscribers': Subscribers,
    }
    return render(request, 'letter/letter.html', context)


def mail_letter(request):
    #emails = Subscribers.objects.values('email')
    #query = None
    #queries = Q(email=query)
    #df = emails
    #read_frame(emails, fieldnames=['email'])
    emails = Subscribers.objects.all()
    df = pd.DataFrame(
        list(
            Subscribers.objects.all().values(
                "email"
            )
        )
    )
    #read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()

    #mail_list = Subscribers.email.values.tolist()
    print(mail_list)
    if request.method == 'GET':
        allMailMessage = MailMessage.objects.all().count()
        newid = allMailMessage + 1
        #form = MailMessageForm(request.POST)
        if 'titleletter' in request.GET:

            title = request.GET['titleletter']
            message = request.GET['messageletter']

            message_new = MailMessage(newid,title,message)
            message_new.save()
            send_mail(
                title,
                message,
                'testsmtpmail@sns-autotransport.com',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('mail-letter')

    context = {
        'MailMessage': MailMessage,
    }
    return render(request, 'letter/mail_letter.html', context)
