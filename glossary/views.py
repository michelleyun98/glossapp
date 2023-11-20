from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Metric

# Create your views here.
def index(request):
    context = {"metrics":Metric.objects.all()}
    return render(request, 'glossary/index.html', context=context)


def metric_detail_view(request, primary_key):
    try:
        metric = Metric.objects.get(pk=primary_key)
        metrics_list = Metric.objects.all()
        context = {
            'metric' : metric,
            'metrics' : metrics_list
        }
    except Metric.DoesNotExist:
        raise Http404(' does not exist')

    return render(request, 'glossary/metric_detail.html', context=context)
    