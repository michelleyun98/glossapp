from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Metric, Intro
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context = {
        "metrics" : Metric.objects.all(),
        "intro" : Intro.objects.latest("created_at"),
    }
    return render(request, 'glossary/index.html', context=context)

def metric_intro_view(request):
    context = {
        "intro" : Intro.objects.latest("created_at"),
        "metrics" : Metric.objects.all()
    }
    return render(request, 'glossary/metric_intro.html', context=context)

def metric_detail_view(request, primary_key):
    try:
        metric = Metric.objects.get(pk=primary_key)
        metrics_list = Metric.objects.all()
        context = {
            "intro" : Intro.objects.latest("created_at"),
            'metric' : metric,
            'metrics' : metrics_list
        }
    except Metric.DoesNotExist:
        raise Http404(' does not exist')

    return render(request, 'glossary/metric_detail.html', context=context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form" : form})
        
        
    
    