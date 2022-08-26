from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'), 
    path('videos/',views.Videos.as_view(), name = 'videos'),
    path('calendario/',views.calendario, name = 'calendario'),
    path('crearcomentario/',views.CrearComentario.as_view(), name='crearcomentario'),
    path('Historias/',views.Historias.as_view(), name ='Historias'),
    path('Integrantes/',views.Integrantes.as_view(), name = 'Equipo'),
    path('GaleriaFotos/',views.Fotos.as_view(),name = 'Imagenes'),
    path('VerImagen/<int:id>/',views.detalleImagen, name='VerFoto'),
    path('registro/',views.registro,name='registro'),
    path('AgregarPosteo/',views.AgregarPosteo.as_view(), name='AgregarPosteo'),
    path('VerPosteo/<int:id>/',views.VerPosteo, name='VerPosteo'),
    path('ComentarPosteo/<int:noticia_id>/',views.ComentarPosteo,name='ComentarPosteo'),
   
]    