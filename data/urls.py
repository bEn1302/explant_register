from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-site'),
    path('', views.start, name="start"),
    path('impressum', views.disclaimer, name="disclaimer"),
    path('dashboard', views.home, name="dashboard"),
    path('analytics', views.all_analytics, name="analytic-explants"),
    path('explants', views.explants_table_view, name="table-explants"),
    path('forms', views.explant_form, name="add-explants"),
    path('search', views.search, name="search"),
]
