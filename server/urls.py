from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from administration.views import patient_fill_form

urlpatterns = [
    path('admin', admin.site.urls),
    path('dashboard', include('administration.urls')),
    path('forms/<str:slug>/<str:form_slug>', patient_fill_form, name='patient-form'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)