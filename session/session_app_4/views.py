from email.policy import default
from django.shortcuts import render

# Create your views here.
def settestcookies(request):
    request.session.set_test_cookie()
    return render(request,'app4/setsession.html')

def checktestcookies(request):
    request.session.test_cookie_worked()
    return render(request,'app4/getsessions.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,'app4/delsession.html')