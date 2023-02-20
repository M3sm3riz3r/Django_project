from urllib import response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Ventas
from .forms import FormVentas

"""
    It gets the object with the id_factura equal to the id passed in the URL, and then deletes it
    """
def eliminar(request,id):    
    obj = Ventas.objects.get(id_factura=id)
  
    if request.method =="GET":        
        obj.delete()        
    
    return HttpResponseRedirect("/ventas/lista")

"""
    It takes a request, creates a context, and then renders a template with that context
    """
def lista(request):     
    context ={}    
    context["dataset"] = Ventas.objects.all()
    return render(request, "consulta.html", context)


"""
    It takes a request object as an argument, and returns a rendered template
    """
def mensaje(request):
    return render(request,"mensaje.html")

# This is a function that is called when the user submits the form. It checks if the form is valid and
# if it is, it saves the data to the database.
def crear_venta(request):
    if request.method == 'POST':        
        form = FormVentas(request.POST)        
        if form.is_valid():            
            
            venta = Ventas(
                id_factura = form.cleaned_data['id_factura'],
                rama= form.cleaned_data['rama'],
                ciudad= form.cleaned_data['ciudad'],
                tipo_cliente= form.cleaned_data['tipo_cliente'],
                genero= form.cleaned_data['genero'],
                linea_de_producto= form.cleaned_data['linea_de_producto'],
                precio_por_unidad= form.cleaned_data['precio_por_unidad'],
                cantidad= form.cleaned_data['cantidad'],
                impuesto= form.cleaned_data['impuesto'],
                total= form.cleaned_data['total'],
                fecha_hora = datetime.now()
            )
            venta.save()
            return HttpResponseRedirect('/ventas/mensaje')
    
    else:
        form = FormVentas()
    return render(request,"formulario.html",{'form': form})


