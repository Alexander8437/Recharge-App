from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.


def index(request):
    return render(request, 'index.html')


def MobileRecharge(request):
    return render(request, 'MobileRecharge.html')


def DthRecharge(request):
    return render(request, 'DthRecharge.html')


def mobileOperator(request, phonenumber):

    roll_number = phonenumber
    return render(request, '/MobileRecharge.html', {'k': roll_number})


def Login(request):
    return render(request, 'Login.html')


def History(request):
    return HttpResponse("This Is about HISTORY.")
