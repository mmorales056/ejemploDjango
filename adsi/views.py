#from .models import Question
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from adsi.models import Aprendiz, Fichas

# Create your views here.
def login(request):
    try:
        user = request.POST['usuario']
        passw= request.POST['clave']
        #Verificar si hay un registro con ese user y ese password
        q = Aprendiz.objects.get(usuario=user, clave=passw)
        #En caso afirmativo se crea variable de sesion
        request.session['logeado'] = [q.nombre,q.apellido,q.id,q.rol]
        return HttpResponseRedirect(reverse('adsi:inicio',args=()))
    except Exception as e:
        return HttpResponse(e)


def logout(request):
    try:
        del request.session['logeado']
        return HttpResponseRedirect(reverse('adsi:inicio',args=()))
    except Exception as e:
        return HttpResponse(e)



def index(request):
    aprendices = 20
    contexto = { 'variable': aprendices }
    return render(request, 'adsi/index.html', contexto)

def aprendizFormulario(request):
    return render(request, 'adsi/aprendiz_formulario.html')

def aprendizGuardar(request):
    try:
        aprendiz = Aprendiz(
            nombre = request.POST['nombre'], 
            apellido = request.POST['apellido'], 
            correo = request.POST['correo'], 
            identificacion = request.POST['identificacion'], 
            usuario = request.POST['usuario'], 
            clave = request.POST['clave'] 
        )
        aprendiz.save()
        return HttpResponseRedirect(reverse('adsi:listarAprendices', args=()))

    except Exception as e:
        return HttpResponse(e)

def aprendizListado(request):
    q = Aprendiz.objects.all() #select * from aprendiz
    contexto = {'datos': q }
    return render(request, 'adsi/aprendiz_listar.html', contexto)

def aprendizEliminar(request, id):
    try:
        q = Aprendiz.objects.get(pk=id)
        q.delete()
        return HttpResponseRedirect(reverse('adsi:listarAprendices', args=()))
    except Exception as e:
        return HttpResponse(e)

def aprendizFormularioEditar(request, id):
    q = Aprendiz.objects.get(pk=id)
    contexto = {'datos': q }
    return render(request, 'adsi/aprendiz_formulario_editar.html', contexto)

def actualizarAprendiz(request):
    try:
        #id del formulario
        id = request.POST['id']
        #consulto el registro con ese id y queda en el objeto q
        q = Aprendiz.objects.get(pk=id)
        #realizo los sets del update
        q.nombre = request.POST['nombre']
        q.apellido = request.POST['apellido']
        q.correo = request.POST['correo']
        q.identificacion = request.POST['identificacion']
        q.usuario = request.POST['usuario']
        q.clave = request.POST['clave']
        #update where objeto q
        q.save()
        return HttpResponseRedirect(reverse('adsi:listarAprendices', args=()))
    except Exception as e:
        return HttpResponse(e)