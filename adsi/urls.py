from django.urls import path

from . import views

app_name = 'adsi'
urlpatterns = [
    path('', views.index, name='inicio'),

    path('crearAprendiz/', views.aprendizFormulario, name='crearAprendiz'),
    path('guardarAprendiz/', views.aprendizGuardar, name='guardarAprendiz'),
    path('listarAprendices/', views.aprendizListado, name='listarAprendices'),
    path('eliminarAprendiz/<int:id>', views.aprendizEliminar, name='eliminarAprendiz'),
    path('editarAprendices/<int:id>', views.aprendizFormularioEditar, name='editarAprendices'),
    path('actualizarAprendiz/', views.actualizarAprendiz, name='actualizarAprendiz'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('verAprendiz/<int:id>', views.verAprendiz, name="verAprendiz"),
    path('verAprendizJson/<int:id>', views.verAprendizJson, name="verAprendizJson"),
    path('reportePdf/', views.reportePdf, name= 'reportePdf'),
    path('crearFicha/', views.formularioFichas, name='formfichas'),
    path('guardarficha',views.guardarFicha, name= 'guardarFicha'),
    path('listarficha', views.fichaListado, name = "listarfichas")


]