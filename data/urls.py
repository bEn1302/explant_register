from django.contrib import admin
from django.urls import path
from . import views

# view_names = [
#     'lagerort_update',
#     'patient_update',
#     'reoperation_update',
#     'inlay_update',
#     'kopf_update',
#     'femurkomponente_update',
#     'schaft_update',
#     'tibiaplateau_update',
#     'pfanne_update',
#     'patellaersatz_update',
# ]

urlpatterns = [
    path('', views.start, name="start"),
    path('impressum', views.disclaimer, name="disclaimer"),
    path('dashboard', views.home, name="dashboard"),
    path('analytics', views.all_analytics, name="analytic-explants"),
    path('explants', views.explants_table_view, name="table-explants"),
    path('forms', views.explant_form, name="add-explants"),
    path('search', views.search, name="search"),
    path('lagerort/<int:pk>/update/', views.lagerort_update, name='lagerort_update'),
    path('patient/<int:pk>/update/', views.patient_update, name='patient_update'),
    path('reoperation/<int:pk>/update/', views.reoperation_update, name='reoperation_update'),
    path('inlay/<int:pk>/update/', views.inlay_update, name='inlay_update'),
    path('kopf/<int:pk>/update/', views.kopf_update, name='kopf_update'),
    path('femurkomponente/<int:pk>/update/', views.femurkomponente_update, name='femurkomponente_update'),
    path('schaft/<int:pk>/update/', views.schaft_update, name='schaft_update'),
    path('tibiaplateau/<int:pk>/update/', views.tibiaplateau_update, name='tibiaplateau_update'),
    path('pfanne/<int:pk>/update/', views.pfanne_update, name='pfanne_update'),
    path('patellaersatz/<int:pk>/update/', views.patellaersatz_update, name='patellaersatz_update'),
] 

# + [
#     path(f'{name}/<int:pk>/update/', getattr(views, name), name=name)
#     for name in view_names
# ]
