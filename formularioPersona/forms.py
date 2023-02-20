from django import forms
from django.core.exceptions import ValidationError
import re

"""
    If the value is not None, then remove all numbers from the value and if there are any numbers left,
    raise a ValidationError, otherwise return the value
    """
def validar_exclucion_numeros(value):
    if value != 'None':
        numeros =  re.sub("[^0-9]", "", value)
        if numeros:
            raise ValidationError("No permite numeros")
        else:
            return value
    return value

# The FormPersonalizado class is a subclass of the forms.Form class. 
# 
# The FormPersonalizado class has four attributes: nombre, apellido, usuario, and ciudad. 
# 
# Each attribute is an instance of the CharField class. 
# 
# The CharField class is a subclass of the Field class. 
# 
# The CharField class has three required arguments: label, max_length, and required. 
# 
# The CharField class has one optional argument: validators. 
# 
# The validators argument is a list of validator functions. 
# 
# The validar_exclucion_numeros function is a validator function. 
# 
# The validar_exclucion_numeros function is a function that raises a ValidationError exception if the
# value of the ciudad attribute contains a number. 
# 
# The validar_ex

class FormPersonalizado(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100,required=True)
    apellido = forms.CharField(label='Apellido', max_length=100)
    usuario = forms.CharField(label='Usuario', max_length=5)
    ciudad = forms.CharField(label='Ciudad', max_length=100,validators =[validar_exclucion_numeros])     
    
    
    """
        It takes all the fields in the form and adds the class 'form-control' to each of them
        """
    def __init__(self, *args, **kwargs):
        super(FormPersonalizado, self).__init__(*args, **kwargs)        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'