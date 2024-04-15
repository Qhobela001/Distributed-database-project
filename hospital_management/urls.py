from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),  # Assuming you have a 'home' view defined in views.py
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/quthing_app/')),
    path('quthing_app/', include('quthing_app.urls')),
]
