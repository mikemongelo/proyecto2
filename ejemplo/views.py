from django.shortcuts import render, redirect
from ejemplo.models import ComentarioPosteo, GaleriaFoto, Noticia , Comentario, Video, Historia,Equipo
from django.views.generic import DetailView,ListView,CreateView,DeleteView,UpdateView
from django.conf import settings 
from .form import ComentarPosteoForm, NoticiasForm, comentarioForm, fotoForm, CustomUserCreationForm 
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login  
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
import datetime
from django.http import  HttpResponse

app_name = 'ejemplo'
# Create your views here

class Inicio(ListView):
  model = Noticia
  form_class = NoticiasForm
  template_name = 'inicio.html'
  paginate_by  = 4

  def get_queryset(self): 
        query = super(Inicio,self).get_queryset().order_by('-id').values()
        return query

class Videos(ListView):
   model = Video
   template_name = 'videos.html'
   
   def  get_queryset(self):
        query = super(Videos,self).get_queryset
        return query 


def calendario(request):    
    return render(request,'calendario.html')

class CrearComentario(CreateView):
    model = Comentario
    form_class  = comentarioForm
    template_name = 'CrearComentario.html'
    success_url = reverse_lazy('inicio')

class Historias(ListView):
    model = Historia
    template_name = 'GaleriaHistorias.html'
    def  get_queryset(self):
        query = super(Historias,self).get_queryset
        return query 

class Integrantes(ListView):
    model = Equipo
    template_name = 'Equipo.html'

    def get_queryset(self):
        query = super(Integrantes,self).get_queryset
        return query

class Fotos(ListView):
    model = GaleriaFoto
    template_name = 'GaleriaFotos.html'

    def get_queryset(self):
        query = super(Fotos,self).get_queryset
        return query

def detalleImagen(request,id):
    imagen = GaleriaFoto.objects.get(id=id)     
    context = {'imagen':imagen}
    return render(request,'VerImagen.html',context)

def registro(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"],
                                password = formulario.cleaned_data["password1"])
            messages.success(request,'Te has registrado correctamente')                    
            login(request,user)                    
            # ir al home
            return redirect(to ='inicio')
        

    return render(request,'registration/registro.html',data)

class AgregarPosteo(CreateView):
    model =  Noticia
    form_class  = NoticiasForm
    template_name = 'AgregarPosteo.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.fecha_de_publicacion = timezone.now()
        return super().form_valid(form)
        
    success_url = reverse_lazy('inicio')


def VerPosteo(request,id):
    noticia = Noticia.objects.get(id=id)     
    comentarios = ComentarioPosteo.objects.filter(posteo=id).order_by('-pk')
    context = {'posteo': noticia,'comentarios': comentarios}
    return render(request,'VerPosteo.html',context)

def ComentarPosteo(request,noticia_id):
    posteo =  Noticia.objects.get(id = noticia_id)
    if request.method == 'POST':
        form = ComentarPosteoForm(request.POST)
        if form.is_valid():
            nComentario = form.save(commit=False)
            nComentario.posteo = posteo
            nComentario.creador = request.user
            nComentario.save() 
            return redirect('VerPosteo',noticia_id) 
    else:    
        form = ComentarPosteoForm()

    
        
    
    
    
       

    

  



    

        
        



