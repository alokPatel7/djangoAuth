from django.shortcuts import render
from authent.models import *

# Create your views here.


def Authentications(req):
    return render(req, 'authentication.html')


def Signup(req):
    if req.method == 'POST':
        firstName = req.POST.get('firstName')
        lastName = req.POST.get('lastName')
        email = req.POST.get('email')
        password = req.POST.get('password')
        UserDetails(
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password
        ).save()
        print("done")
    return render(req, 'landingpage.html')


def Login(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')
        try:
            data = UserDetails.objects.get(
                email=email,
                password=password
            )
            req.session['currentUserName'] = data.firstName
        except:
            return render(req, 'authentication.html')
    return render(req, 'landingpage.html')
