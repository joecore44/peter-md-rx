from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from administration.views import patient_fill_form, update_patient_form, log_in

urlpatterns = [
    path('admin', admin.site.urls),
    path('login', auth_views.LoginView.as_view(template_name='content/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='content/logout.html'), name='logout'),
    path('dashboard', include('administration.urls')),
    path('forms/<str:slug>/<str:form_slug>', patient_fill_form, name='patient-form'),
    path('api/update/<str:slug>/<str:field>/<str:val>', update_patient_form, name='update-patient-form'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)