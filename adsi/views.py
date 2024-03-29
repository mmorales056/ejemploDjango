#Libreria para sacar las rutas relativas del SO
import os
#Libreria para reportes en pdf
from django.template.loader import get_template
from .utils import render_to_pdf

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from adsi.models import Aprendiz, Fichas
from django.forms.models import model_to_dict

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
    ses = request.session.get('logeado',False)
    if ses and (ses[3]=="2"):
        return render(request, 'adsi/aprendiz_formulario.html')
    else:
        contexto={'s': 'fallo'}
        return render(request, 'adsi/index.html',contexto)

def aprendizGuardar(request):
    try:
        aprendiz = Aprendiz(
            nombre = request.POST['nombre'], 
            apellido = request.POST['apellido'], 
            correo = request.POST['correo'], 
            identificacion = request.POST['identificacion'], 
            usuario = request.POST['usuario'], 
            clave = request.POST['clave'],
            rol= request.POST['rol']
        )
        aprendiz.save()
        return HttpResponseRedirect(reverse('adsi:listarAprendices', args=()))

    except Exception as e:
        return HttpResponse(e)

def guardarFicha(request):
    try:
        q = Aprendiz.objects.get(pk=request.POST['aprendiz'])
        ficha = Fichas(
            aprendiz = q,
            codigo = request.POST['codigo'],
            programa = request.POST['programa']            
        )
        ficha.save()
        return render(request, 'adsi/index.html')
    except Exception as e:
        return HttpResponse(e)

def aprendizListado(request):
    ses = request.session.get('logeado',False)
    if ses and (ses[3]=='1' or ses[3]=='2'):
        q = Aprendiz.objects.all() #select * from aprendiz
        contexto = {'datos': q }
        return render(request, 'adsi/aprendiz_listar.html', contexto)
    else:
        return HttpResponse("No tiene permisos para ver el listado")

def fichaListado(request):
    q = Fichas.objects.all()
    contexto = {'fichas': q}
    return render(request, 'adsi/fichas_listar.html', contexto)
    


def formularioFichas(request):
    q = Aprendiz.objects.all()
    contexto= {'aprendices': q}    
    return render(request, 'adsi/formulario_fichas.html',contexto)


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
        q.rol = request.POST['rol']
       
        #update where objeto q
        q.save()
        return HttpResponseRedirect(reverse('adsi:listarAprendices', args=()))
    except Exception as e:
        return HttpResponse(e)

def verAprendiz(request, id):
    try:
        q = Aprendiz.objects.get(pk=id)
        return render(request,'adsi/aprendiz_ver.html', { 'aprendiz':q })
    except Exception as e:
        return HttpResponse(e)

def verAprendizJson(request, id):
    try:
        q = Aprendiz.objects.get(pk=id)
        diccionario = model_to_dict(q)
        return JsonResponse(diccionario)
    except Exception as e:
        return HttpResponse(e)

def reportePdf(request):
    consulta= Aprendiz.objects.all()
    contexto={'datos': consulta}
    
    pdf = render_to_pdf('adsi/reporte.html', contexto)
    
    response = HttpResponse(pdf,content_type='application/pdf')
    #response['Content-Disposition'] ='attachment; filename=Reporte.pdf' con este se guarda el pdf
    response['Content-Disposition'] = 'filename=Reporte.pdf'
    return response


    

