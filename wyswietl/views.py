from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import OdbiorcaForm
from .forms import ParametryForm
from .models import Odbiorca
from .models import Parametry
from .forms import UOAP0Form
from .models import UOAP0
from .models import UOAP2
from .forms import UOAP2Form



def widok(request):
    return render('To jest test <b>tekst</b>')

def testowywidok(request):
    post=Odbiorca.objects.all().last()
    parametry=Parametry.objects.all().last()
    return render(request,'test.html',{'parametry':parametry})

def mainwebsite(request):    
   if request.method == "POST":
       form=OdbiorcaForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect(editProject)
   else:
       form=OdbiorcaForm()
   return render(request,'mainwebsite.html',{'form':form})


def editProject(request):
    if request.method == "POST":
       form=ParametryForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect(testowywidok) 
    else:
        form=ParametryForm()
    return render(request,'edit.html',{'form':form})


def major(request):
    return render_to_response('maina.html')

def uoap0odbiorca(request):
    if request.method =="POST":
       form=OdbiorcaForm(request.POST)
       if form.is_valid():
              form.save()
              return redirect(uoap0forms)
    else:
       form=OdbiorcaForm()
    return render(request,'mainwebsite.html',{'form':form})

def uoap0forms(request):
    if request.method == "POST":
       form=UOAP0Form(request.POST)
       if form.is_valid():
            form.save()
            return redirect(uoapp0widok)
    else:
        form=UOAP0Form()
    return render(request,'uoapp0.html',{'form':form})

def uoa(request):
    return render_to_response('uoaprojects.html')


def uoapp0widok(request):
     post=Odbiorca.objects.all().last()
     parametry=UOAP0.objects.all().last()
     return uoapp0(request,'test.html',{'uoap0':parametry})



def uoap2odbiorca(request):
    if request.method =="POST":
       form=OdbiorcaForm(request.POST)
       if form.is_valid():
              form.save()
              return redirect(uoap2forms)
    else:
       form=OdbiorcaForm()
    return render(request,'mainwebsite.html',{'form':form})

def uoap2forms(request):
    if request.method == "POST":
       form=UOAP2Form(request.POST)
       if form.is_valid():
            form.save()
            return redirect(uoapp2widok)
    else:
        form=UOAP2Form()
    return render(request,'uoapp2.html',{'form':form})

def uoapp2widok(request):
     post=Odbiorca.objects.all().last()
     parametry=UOAP2.objects.all().last()
     return uoapp0(request,'uoap2result.html',{'uoap2':parametry})

