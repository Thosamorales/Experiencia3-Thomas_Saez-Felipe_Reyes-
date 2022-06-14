from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm
from .models import Inventario
from .forms import InventarioForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def formulario(request):
    return render(request, 'formulario.html')
    
def formularioRE(request):
    return render(request, 'formularioRE.html')
    
def Galeria(request):
    return render(request, 'Galeria.html')

def herramienta(request):
    return render(request, 'herramienta.html')

def moneda(request):
    return render(request, 'moneda.html')

def quinesSomos(request):
    return render(request, 'quinesSomos.html')

def tierra(request):
    return render(request, 'tierra.html')

def inicioAdmin(request):
    return render(request, 'inicioAdmin.html')

def mostrar(request):
    colaboradores = Colaborador.objects.all()

    datos = {
        'colaboradores': colaboradores
    }
    return render(request, 'mostrar.html', datos)


def form_crear_colaborador(request):
    if request.method=='POST': 
        colaborador_form = ColaboradorForm(request.POST)
        if colaborador_form.is_valid:
            colaborador_form.save()
            return redirect ('mostrar')
    else:
        colaborador_form =ColaboradorForm()
    return render(request, 'form_crear_colaborador.html', {'colaborador_form': colaborador_form})

def form_mod_colaborador(request,id):
    colaborador = Colaborador.objects.get(rut=id)
    datos={
        'form': ColaboradorForm(instance=colaborador)
    }
    if request.method=='POST':
        formulario=ColaboradorForm(data=request.POST, instance=colaborador)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    
    return render(request, 'form_mod_colaborador.html', datos)




def form_del_colaborador(request, id):
    colaborador = Colaborador.objects.get(rut=id)
    colaborador.delete()
    return redirect('mostrar')



def inventario(request):
    inventario = Inventario.objects.all()

    datos = {
        'Inventario': inventario
    }
    return render(request, 'inventario.html', datos)


def inventarioCrear(request):
    if request.method=='POST': 
        Inventario_Form = InventarioForm(request.POST, files=request.FILES)
        if Inventario_Form.is_valid:
            Inventario_Form.save()
            return redirect ('inventario')
    else:
        Inventario_Form = InventarioForm()
    return render(request, 'inventarioCrear.html', {'Inventario_Form': InventarioForm})

def inventarioMod(request, id): 
    inventario = Inventario.objects.get(codigo=id)
    datos = {
        'form': InventarioForm(instance=inventario)
    }
    if request.method=='POST':
        formulario = InventarioForm(data = request.POST, instance=inventario, files=request.FILES)
        if formulario.is_valid: 
            formulario.save()
            data['form'] = InventarioForm(instance=Inventario.objects.get(codigo=id))
            return redirect ('inventario')
    return render (request, 'inventarioMod.html', datos )


def inventario_del(request, id):
    inventario = Inventario.objects.get(codigo=id)
    inventario.delete()
    return redirect('inventario')







