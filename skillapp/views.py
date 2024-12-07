import json

import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.template.context_processors import request
from requests.auth import HTTPBasicAuth

from skillapp.credentials import MpesaAccessToken, LipanaMpesaPpassword

from skillapp.models import Profile

# Create your views here.
def index(request):
    return render(request,'index.html')

def author(request):
    return render(request,'author.html')

def explore(request):
    return render(request,'explore.html')

def aisha(request):
    return render(request,'aisha.html')
def grace(request):
    return render(request,'grace.html')
def brian(request):
    return render(request,'brian.html')
def ama(request):
    return render(request,'ama.html')
def example(request):
    return render(request,'example.html')
def create(request):
    if request.method == 'POST':
        myprofiles=Profile(
            name = request.POST['name'],
            email = request.POST['email'],
            password = request.POST['password'],
            about = request.POST['about'],
            experience = request.POST['experience'],
            role = request.POST['role'],
            fee = request.POST['fee'],
            duration = request.POST['duration'],
            contact = request.POST['contact'],
            specialty = request.POST['specialty'],
            interest = request.POST['interest'],
            phone = request.POST['phone'],
            image = request.FILES['image']
        )
        myprofiles.save()
        return redirect('/create')

    else:
        return render(request,'create.html')

def aishaaccount(request):

    profile = Profile.objects.all()
    return render(request, 'aishaaccount.html', {'profile': profile})






def token(request):
    consumer_key = 'yOxGzgvH8T6Hs3zydV8dXnDzz1NyWS0s8X1pNGXjHg4JAfR7'
    consumer_secret = '3DTJgjXHwvMMyvAodbwmNWef5VmAlzsLBKVVfo6UlgXxRrUed2IhYAO4QyKMYoJG'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "SkillBridge",
            "TransactionDesc": "<Mentorship>"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")






