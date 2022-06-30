from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from .views import BlogListView,BlogCreateView, BlogdetailView,BlogUpdateView,BlogDeleteView

app_name='blog'

urlpatterns = [
    
    path('',BlogListView.as_view(),name='home'),#?creamos la vista listar y se la asignamos a la url de blog
    path('create/',BlogCreateView.as_view(),name='create'), #?creamos la vista a create y se la asignamos a la url de blog
    path('<int:pk>/',BlogdetailView.as_view(),name='detail'), #?Creamos la vista detalle del blog
    path('<int:pk>/update/',BlogUpdateView.as_view(),name='update'), #?en esta url actualizamos
    path('<int:pk>/delete/',BlogDeleteView.as_view(),name='delete'), #?en esta url eliminamos
    
]


