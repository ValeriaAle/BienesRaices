from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from inmuebles.models import Casa, cliente, ficha_tecnica

# Create your views here.

#def casa(request):

 #     casa =  Casa(numero="Desarrollo web", camada="19881")
  #    casa.save()
   #   documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


    #  return HttpResponse(documentoDeTexto)


def home(request):

      return render(request, "inmuebles/home.html")

def casa(request):

      return render(request, "inmuebles/casa.html")

def ficha_tecnica(request):

      return render(request, "inmuebles/ficha_tecnica.html")


def clientes(request):

      return render(request, "inmuebles/clientes.html")



from inmuebles.forms import CasaFormulario

def casaFormulario(request):
      if request.method == "POST":
            miFormulario = CasaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  casa = Casa(numero=informacion["numero"], categoria=informacion["categoria"], domicilio=informacion["domicilio"], tipo=informacion["tipo"], fecha_disponible=informacion["fecha_disponible"], detalle=informacion["detalle"])
                  casa.save()
                  return render(request, "inmuebles/home.html")
            else:
                  miFormulario = CasaFormulario()
                  return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
      return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
      respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
      
      #No olvidar from django.http import HttpResponse 
      return HttpResponse(respuesta)
