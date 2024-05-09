
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='pagina_principal'),
    path('login/', views.login, name='iniciar_sesion'),

    #includes
    path("usuarios/", include('app.usuarios.urls'))
]
