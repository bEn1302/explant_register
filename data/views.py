from django.shortcuts import render
from .models import Explantat
from django.http import HttpResponseRedirect
from .forms import *

def start(request):
    return render(request, 'startpage/index.html')

def home(request):
    return render(request, 'data/dashboard.html')

def explants_table_view(request):
    huefte_explant_table = Explantat.objects.filter(kopf__isnull=False, pfanne__isnull=False, schaft__isnull=False)
    knie_explant_table = Explantat.objects.filter(femurkomponente__isnull=False, tibiaplateau__isnull=False, patellaersatz__isnull=False)

    context = {
        'huefte_explant_table': huefte_explant_table,
        'knie_explant_table': knie_explant_table,
    }

    return render(request, 'data/explant_table.html', context)

def all_analytics(request):
    return render(request, 'data/explant_analytic.html')

def explant_form(request):
    submitted = False
    if request.method == "POST":
        form = FemurkomponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/forms?submitted=True')
    else:
        form = FemurkomponenteForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'data/explant_form.html', {'form':form, 'submitted':submitted})

#def all_explants(request):
#    explant_table = Explantat.objects.all()
#    return render(request, 'data/explant_table.html',{'explant_table': explant_table})