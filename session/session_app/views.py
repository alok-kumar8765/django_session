from email.policy import default
from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Alok'
    request.session['mname']='kumar'
    return render(request,'app/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name',default='Guest')
    mname = request.session.get('mname',default='Guest')
    return render(request,'app/getsession.html',{'name':name,'mname':mname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'app/delsession.html')