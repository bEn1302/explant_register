from django.shortcuts import render
from .models import Explantat
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import redirect
from .forms import *

def start(request):
    return render(request, 'startpage/index.html')

def home(request):
    return render(request, 'data/dashboard.html')

def disclaimer(request):
    return render(request, 'startpage/impressum.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # search results
        huefte_explants = Explantat.objects.filter(ursache__icontains=searched, kopf__isnull=False, pfanne__isnull=False, schaft__isnull=False)
        knie_explants = Explantat.objects.filter(ursache__icontains=searched, tibiaplateau__isnull=False, patellaersatz__isnull=False)
        return render(request, 'data/search.html', {'searched': searched, 'huefte_explants':huefte_explants, 'knie_explants':knie_explants})
    else:
        return render(request, 'data/search.html', {})


def explants_table_view(request):
    huefte_explant_table = Explantat.objects.filter(kopf__isnull=False, pfanne__isnull=False, schaft__isnull=False)
    knie_explant_table = Explantat.objects.filter(femurkomponente__isnull=False, tibiaplateau__isnull=False, patellaersatz__isnull=False)

    context = {
        'huefte_explant_table': huefte_explant_table,
        'knie_explant_table': knie_explant_table,
    }

    return render(request, 'data/explant_table.html', context)



def lagerort_update(request, pk):
    lagerort = Lagerort.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = LagerortUpdateForm(request.POST, instance=lagerort)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
    else:
        form = LagerortUpdateForm(instance=lagerort)
        response_data = {'success': False}

    # Überprüfen Sie den HTTP_X_REQUESTED_WITH-Header, um festzustellen, ob die Anfrage über AJAX erfolgte
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        # Wenn die Anfrage nicht über AJAX erfolgte, leiten Sie zur "table-explants"-Seite um
        return redirect('table-explants')




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
