from django.shortcuts import redirect, render
from .forms import Formpersona, ContactoForm
from .models import persona
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request,'persona/index.html')

def listado(request):
    personas = persona.objects.all()
    return render(request,'persona/listado.html', {"personas":personas})

def nueva(request):
    if request.method == "POST":
        formpersona = Formpersona(request.POST)
        if formpersona.is_valid():
            formpersona.save()
            return redirect('listado')
    else:
        formpersona = Formpersona()
        return render(request, 'persona/nueva.html',{"formpersona": formpersona})
    
    
def editar(request):
    Persona= get_object_traceback
    
    
    
def contacto(request):
    contactoform = ContactoForm()
    if request.method == "POST":
        contactoform = ContactoForm(request.POST)
        if contactoform.is_valid():
            nombre = request.POST["nombre"]
            email = request.POST["email"]
            mensaje = request.POST["mensaje"]            
    

def persona_paginacion(request):
    personas = persona.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(personas, 5)  #  paginate_by 5
    try:
        personas = paginator.page(page)
    except PageNotAnInteger:
        personas = paginator.page(1)
    except EmptyPage:
        personas = paginator.page(paginator.num_pages)
    return render(request, "persona/persona_paginacion.html", {"personas": personas})
    
    

# Create your views here.
