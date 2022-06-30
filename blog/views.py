
# todo: Vistas

from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.views.generic import View, UpdateView, DeleteView

#! traemos la clase de froms.py PostCreateForm
from .forms import PostCreateForm
from .models import Post

#! importamos de django
from django.urls import reverse_lazy


#todo esta clase es para listar los blog
class BlogListView(View):
    def get(self,request,*args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request,'blog_list.html',context)


#todo esta clase crea la vista al BlogCreateView
class BlogCreateView(View):
    
    def get(self,request,*args, **kwargs):
        form=PostCreateForm() #?pasamos la clase form de traida de forms.py a una variable llamada form
        context={
            'form':form
        }
        return render(request,'blog_create.html',context)
    
    #todo el get los cambiamos a post dentro de la misma clase
    def post(self,request,*args, **kwargs):
        
        if request.method == "POST": #?si el metodo es post
            form=PostCreateForm(request.POST) #? traeme el formulario y toda la info que esta dentro de post(request.POST) en el formulario en la pagina create
            
            if form.is_valid(): #? si el formulario es valido obtenemos el titulo y el contenido la info que ingresamos en la pagina create
                title = form.cleaned_data.get('title') #? aqui obtenemos lo que ingresamos en el campo title del formulario
                content = form.cleaned_data.get('content') #? aqui obtenemos lo que ingresamos en el campo content del formulario
                
                
                p,created = Post.objects.get_or_create(title=title, content=content) #? Al modelo Post (BBDD) le asiganamos lo que tenemos en el formulario
                p.save() #? guardamos la informacion en el modelo de la BBDD
                return redirect('blog:home') #? lo redireccionamos al home
            
        context={
            
        }
        return render(request,'blog_create.html',context)
    
    
#todo esta clase crea el detalle del blog   
class BlogdetailView(View):
    def get(self,request,pk,*args, **kwargs):
        post = get_object_or_404(Post, pk=pk) #?creamos el objeto post y llamamos al modelo Post y su prymary key = pk,
                                              #?y la igualamos con la que viene de la url --> path('<int:pk>/',BlogdetailView.as_view(),name='detail')
        context = {
            'post':post
        }
        return render(request,'blog_detail.html',context)
    
#todo esta clase actualizara el blog
class BlogUpdateView(UpdateView):
    model = Post  #? le pasamos el modelo que queremos editar
    fields=['title','content'] #? pasamos los campos que queremos editar
    template_name='blog_update.html' #? lo enviamos al blog_update.html
    
    def get_success_url(self):     #? una vez lo actualizamos lo redireccionamos al blog:detail
        pk = self.kwargs['pk'] #?creamos un objeto del modelo Post ese objeto es self y traemos la kwargs y su campo pk
        return reverse_lazy('blog:detail', kwargs={'pk':pk})
    
#todo esta clase borra un blog
class BlogDeleteView(DeleteView):
    model = Post  #? le pasamos el modelo que queremos editar
    template_name='blog_delete.html' #? lo enviamos al blog_delete.html
    success_url= reverse_lazy('blog:home')