

# todo: Formulario

# !libreria de django para formularios
from dataclasses import field, fields
from django import forms

# !traemos el modelo de blogs
from .models import Post


# !Formulario para crear un post desde la vista a la BBDD
class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post # *traemos el modelo
        fields=('title','content') # *traemos los campos del modelo
            

