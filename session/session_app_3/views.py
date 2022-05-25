from email.policy import default
from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Alok'
    request.session.set_expiry(60)
    return render(request,'app3/setsession.html')

def getsession(request):
    name = request.session['name']
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request,'app3/getsessions.html',
    {'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'app3/delsession.html')