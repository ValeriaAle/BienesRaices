from django import forms

class CasaFormulario(forms.Form):
    #especificar los campos
   
    numero = forms.IntegerField()
    categoria= forms.CharField()
    domicilio= forms.CharField()
    tipo= forms.CharField()
    fecha_disponible= forms.DateField()  
    detalle= forms.CharField() 