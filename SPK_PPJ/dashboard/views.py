from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from knnApp.models import DataTesting, DataTraining
from account.models import MyUser

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):

    training = DataTraining.objects.all().count()
    data = DataTesting.objects.all().count()
    rpl_testing = DataTesting.objects.filter(peminatan=2).count()
    mm_testing = DataTesting.objects.filter(peminatan=1).count()
    jarkom_testing = DataTesting.objects.filter(peminatan=0).count()
    rpl_training = DataTraining.objects.filter(peminatan='RPL').count()
    mm_training = DataTraining.objects.filter(peminatan='MM').count()
    jarkom_training = DataTraining.objects.filter(peminatan='Jarkom').count() 
    pengguna = MyUser.objects.all().count()
    context = {
        'data': data,
        'rpl_training': rpl_training,
        'mm_training': mm_training,
        'jarkom_training': jarkom_training,
        'rpl_testing': rpl_testing,
        'mm_testing': mm_testing,
        'jarkom_testing': jarkom_testing,
        'pengguna': pengguna,
        'training': training,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    context = {
        
    }
    return render(request, 'dashboard/dashboard.html', context)

