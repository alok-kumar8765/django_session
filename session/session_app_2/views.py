from email.policy import default
from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Alok'
    request.session['mname']='kumar'
    return render(request,'app/setsession.html')

def getsession(request):
    name = request.session.get('name',default='Guest')
    key = request.session.keys()
    items = request.session.items()
    age=request.session.setdefault('age','26')
    return render(request,'app/getsessions.html',
    {'name':name,'key':key,'items':items,'age':age})

def delsession(request):
    request.session.flush()
    return render(request,'app/delsession.html')