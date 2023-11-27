from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Metric, Intro, Feature
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from scripts import module

class ContextDict:
    cd = {
        "metrics" : Metric.objects.all(),
        "intro" : Intro.objects.latest("created_at"),
        "index":False
    }
   
    def __init__(self, **kwargs):
        for kw in kwargs:
            self.cd[str(kw)] = kwargs[kw]

# Create your views here.
def index(request):
    context = ContextDict(index=True)
    return render(request, 'glossary/index.html', context=context.cd)

def metric_intro_view(request):
    context = ContextDict(index=False)
    #context.update(index=False)
    return render(request, 'glossary/metric_intro.html', context=context.cd)

def metric_detail_view(request, primary_key):
    try:
        metric = Metric.objects.get(pk=primary_key)
        context = ContextDict(index=False, metric=metric)
        #context.update(index=False, metric=Metric.objects.get(pk=primary_key))
    except Metric.DoesNotExist:
        raise Http404(' does not exist')

    return render(request, 'glossary/metric_detail.html', context=context.cd)

def feature_detail_view(request, feature_name):
    try:
        
        fname = module.to_text(feature_name)
        feature = Feature.objects.get(name=fname)
        
        metric = feature.metric.all().get()
        context = ContextDict(feature=feature, metric=metric)
        #context.update(index=False, metric=Metric.objects.get(pk=primary_key))
    except Feature.DoesNotExist:
        raise Http404(' does not exist')

    return render(request, 'glossary/feature_detail.html', context=context.cd)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form" : form})
        
        
    
    