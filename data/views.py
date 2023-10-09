from django.shortcuts import render, redirect, get_object_or_404
from .models import Explantat
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect

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


# Update
def lagerort_update(request, pk):
    lagerort = get_object_or_404(Lagerort, pk=pk)
    
    if request.method == 'POST':
        form = LagerortUpdateForm(request.POST, instance=lagerort)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = LagerortUpdateForm(instance=lagerort)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')

# hier übergebe ich noch form: form...
# def patient_update(request, pk):
#     patient = get_object_or_404(Patient, pk=pk)
    
#     if request.method == 'POST':
#         form = PatientUpdateForm(request.POST, instance=patient)
#         if form.is_valid():
#             form.save()
#             response_data = {'success': True}
#         else:
#             response_data = {'success': False, 'errors': form.errors}
#             return HttpResponseBadRequest(JsonResponse(response_data))
#     else:
#         form = PatientUpdateForm(instance=patient)
#         response_data = {'success': False}

#     if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         return JsonResponse(response_data)
#     else:
#         return redirect('table-explants', {'patient_form':form, 'response_data': response_data})
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PatientUpdateForm(instance=patient)
        return render(request, 'data/explant_table.html', {'form': form, 'patient': patient})


def reoperation_update(request, pk):
    reoperation = get_object_or_404(Reoperation, pk=pk)
    
    if request.method == 'POST':
        form = ReoperationUpdateForm(request.POST, instance=reoperation)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = ReoperationUpdateForm(instance=reoperation)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')

def inlay_update(request, pk):
    inlay = get_object_or_404(Inlay, pk=pk)
    
    if request.method == 'POST':
        form = InlayUpdateForm(request.POST, instance=inlay)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = InlayUpdateForm(instance=inlay)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')
    
def kopf_update(request, pk):
    kopf = get_object_or_404(Kopf, pk=pk)
    
    if request.method == 'POST':
        form = KopfUpdateForm(request.POST, instance=kopf)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = KopfUpdateForm(instance=kopf)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')

def femurkomponente_update(request, pk):
    femurkomponente = get_object_or_404(Femurkomponente, pk=pk)
    
    if request.method == 'POST':
        form = FemurkomponenteUpdateForm(request.POST, instance=femurkomponente)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = FemurkomponenteUpdateForm(instance=femurkomponente)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')
    
def schaft_update(request, pk):
    schaft = get_object_or_404(Schaft, pk=pk)
    
    if request.method == 'POST':
        form = SchaftUpdateForm(request.POST, instance=schaft)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = SchaftUpdateForm(instance=schaft)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')
    
def tibiaplateau_update(request, pk):
    tibiaplateau = get_object_or_404(Tibiaplateau, pk=pk)
    
    if request.method == 'POST':
        form = TibiaplateauUpdateForm(request.POST, instance=tibiaplateau)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = TibiaplateauUpdateForm(instance=tibiaplateau)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')

def pfanne_update(request, pk):
    pfanne = get_object_or_404(Pfanne, pk=pk)
    
    if request.method == 'POST':
        form = PfanneUpdateForm(request.POST, instance=pfanne)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = PfanneUpdateForm(instance=pfanne)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')

def patellaersatz_update(request, pk):
    patellaersatz = get_object_or_404(Patellaersatz, pk=pk)
    
    if request.method == 'POST':
        form = PatellaersatzUpdateForm(request.POST, instance=patellaersatz)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = PatellaersatzUpdateForm(instance=patellaersatz)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
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
