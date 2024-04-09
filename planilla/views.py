from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Presupuesto, Cliente

from .forms import PresupuestoForm, ClienteForm

def home(request):
    return render(request, 'home.html')
########MOSTAR######
def listaPres(request):
    servicios= Presupuesto.objects.all()
    return render(request, 'listaPres.html',{'servicios': servicios})   

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'clientes.html',
                  {'clientes':clientes})
#######BUSQUEDA########


#####FORMULARIO CREATE#####


def create_pres(request):
    foms = PresupuestoForm
    if request.method=='POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaPres')
    else:
        form = PresupuestoForm()
    return render(request, 'create_pres.html',{'form':form})                  


def create_cli(request):
    foms= ClienteForm
    if request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form =  ClienteForm()
    return render(request, 'create_cli.html',{'form':form})                  

def update(request,pk):
    presupuesto= get_object_or_404(Presupuesto, id= pk)
    form = PresupuestoForm(initial={'titulo':presupuesto.titulo,'materiaPrima':presupuesto.materiaPrima, 'manoDeObra':presupuesto.manoDeObra, 'fecha':presupuesto.fecha, 'precio':presupuesto.precio,'estado':presupuesto.estado})
    if request.method == "POST":
        form = PresupuestoForm(request.POST)
        if form.is_valid():
                                    #CLEANED=limpia datos de los campos##                                   
            form.save()
           
            return redirect('listaPres')
        else:
           print("error")
    else:        
        return render(request,
              'create_pres.html',  
              {'form':form}  
              )

