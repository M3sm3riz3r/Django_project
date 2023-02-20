#from django.contrib import admin
#from django.urls import path,include
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('formulario/', include('webventas.urls')),
    path('formulario', views.formulario, name='formulario2'),
]