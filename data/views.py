from django.shortcuts import render, redirect, get_object_or_404
from .models import *
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

# --------------------------- Effizientere Version ? ----------------------------
# 
# 
# def update_model(request, model_cls, form_cls, redirect_url):
#     obj = get_object_or_404(model_cls, pk=pk)
    
#     if request.method == 'POST':
#         form = form_cls(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#             response_data = {'success': True}
#         else:
#             response_data = {'success': False, 'errors': form.errors}
#             return HttpResponseBadRequest(JsonResponse(response_data))
#     else:
#         form = form_cls(instance=obj)
#         response_data = {'success': False}

#     if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         return JsonResponse(response_data)
#     else:
#         return redirect(redirect_url)

# def lagerort_update(request, pk):
#     return update_model(request, Lagerort, LagerortUpdateForm, 'table-explants')

# def patient_update(request, pk):
#     return update_model(request, Patient, PatientUpdateForm, 'table-explants')

#  Fügen Sie hier weitere ähnliche Funktionen hinzu
# 
# 
# -------------------------------------------------------------------------------



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

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = PatientUpdateForm(instance=patient)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('table-explants')

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


# Data Insert
def explant_form(request):
    if request.method == 'POST' or None:
        explantat_form = ExplantatForm(request.POST or None, request.FILES)
        lagerort_form = LagerortForm(request.POST or None)  # Lagerort-Formular
        patient_form = PatientForm(request.POST or None)  # Patient-Formular
        reoperation_form = ReoperationForm(request.POST or None)  # Reoperation-Formular
        inlay_form = InlayForm(request.POST or None)  # Inlay-Formular
        kopf_form = KopfForm(request.POST or None)  # Kopf-Formular
        femurkomponente_form = FemurkomponenteForm(request.POST or None)  # Femurkomponente-Formular
        schaft_form = SchaftForm(request.POST or None)  # Schaft-Formular
        tibiaplateau_form = TibiaplateauForm(request.POST or None)  # Tibiaplateau-Formular
        pfanne_form = PfanneForm(request.POST) # Pfanne-Formular
        patellaersatz_form = PatellaersatzForm(request.POST or None) # Patellaersatz-Formular

        if explantat_form.is_valid() and lagerort_form.is_valid() and patient_form.is_valid() and reoperation_form.is_valid() and inlay_form.is_valid() and kopf_form.is_valid() and femurkomponente_form.is_valid() and schaft_form.is_valid() and tibiaplateau_form.is_valid() and pfanne_form.is_valid() and patellaersatz_form.is_valid():
            explantat = explantat_form.save(commit=False)
            lagerort = lagerort_form.save()
            patient = patient_form.save()
            reoperation = reoperation_form.save()
            inlay = inlay_form.save()
            kopf = kopf_form.save()
            femurkomponente = femurkomponente_form.save()
            schaft = schaft_form.save()
            tibiaplateau = tibiaplateau_form.save()
            pfanne = pfanne_form.save()
            patellaersatz = patellaersatz_form.save()

            # Setzen Sie die Verknüpfung von Explantat zu Inlay
            explantat.patellaersatz = patellaersatz
            explantat.pfanne = pfanne
            explantat.tibiaplateau = tibiaplateau
            explantat.schaft = schaft
            explantat.femurkomponente = femurkomponente
            explantat.kopf = kopf
            explantat.inlay = inlay
            explantat.reoperation = reoperation
            explantat.patient = patient
            explantat.lagerort = lagerort
            explantat.save()
            
            # Weiterleitung zur Erfolgsseite oder zur Liste der Explantate
            return redirect('table-explants')

    else:
        explantat_form = ExplantatForm()
        lagerort_form = LagerortForm()
        patient_form = PatientForm()
        reoperation_form = ReoperationForm()
        inlay_form = InlayForm()
        kopf_form = KopfForm()
        femurkomponente_form = FemurkomponenteForm()
        schaft_form = SchaftForm()
        tibiaplateau_form = TibiaplateauForm()
        pfanne_form = PfanneForm()
        patellaersatz_form = PatellaersatzForm()

    return render(request, 'data/explant_form.html', {'explantat_form': explantat_form,
                                                      'lagerort_form':lagerort_form,
                                                      'patient_form':patient_form,
                                                      'reoperation_form':reoperation_form, 
                                                      'inlay_form': inlay_form,
                                                      'kopf_form':kopf_form,
                                                      'femurkomponente_form':femurkomponente_form,
                                                      'schaft_form':schaft_form,
                                                      'tibiaplateau_form':tibiaplateau_form,
                                                      'pfanne_form':pfanne_form,
                                                      'patellaersatz_form':patellaersatz_form,
                                                      })
