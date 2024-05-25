from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('data.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),

    path('captcha/', include('captcha.urls')),
    path('rosetta/', include('rosetta.urls')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

