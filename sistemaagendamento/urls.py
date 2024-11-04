from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_about(request):
    return redirect('about')  # Redireciona para a página "Sobre" do app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointment_system/', include('appointment_system.urls')),  # Incluindo as URLs do app
    path('', redirect_to_about),  # Redireciona a raiz para a página "Sobre"
]
