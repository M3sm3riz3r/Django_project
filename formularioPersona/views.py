from django.shortcuts import render
from . import forms

# Create your views here.
def formulario(request):
    contexto = {"estado":""}
    if request.method == 'POST': 
        form = forms.FormPersonalizado(request.POST)   
        if form.is_valid():
            contexto["estado"] = "success"
    else:
        form = forms.FormPersonalizado()
    return render(request,"formulario2.html",{'form': form,'contexto':contexto})

from django.shortcuts import render
from . import forms

