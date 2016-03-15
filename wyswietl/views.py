from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import OdbiorcaForm
from .forms import ParametryForm
from .models import Odbiorca
from .models import Parametry

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
