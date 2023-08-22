from django.shortcuts import render

# Pull Data from Datatable:
from .models import Explantat
from .models import Femurkomponente

# Create your views here.

def kopf_view(request):
    femurcomponent_data = Femurkomponente.objects.all()
    context = {'femurcomponent_data': femurcomponent_data}
    return render(request, 'data/explant_table.html', context)

def all_analytics(request):
    return render(request, 'data/explant_analytic.html')

def all_explants(request):
    explant_table = Explantat.objects.all()
    return render(request, 'data/explant_table.html',{'explant_table': explant_table})

def home(request):
    return render(request, 'data/home.html')