from django.shortcuts import render

# Pull Data from Datatable:
from .models import Explantat

# Create your views here.
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

def home(request):
    return render(request, 'data/home.html')