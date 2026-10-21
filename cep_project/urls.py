"""
URL configuration for cep_project project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from cep_app.views import export_quotes_csv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cep_app.urls')),
    path('api-token-auth/', obtain_auth_token), 
    path('api/export-quotes/', export_quotes_csv),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)