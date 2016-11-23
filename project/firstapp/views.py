from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Post

from django.http import HttpResponse

def index(request):
    return render(request, 'firstapp/index.html')
    #liaison entre index et view pour afficher e contenu de index ds le navigateur

def index2(request):
    return render(request, 'firstapp/index2.html')
def acceuil(request):
    return render(request, 'firstapp/acceuil.html')
#def contact(request):
#    return render(request, 'firstapp/contact.html')


class PostDetail(DetailView):
    model = Post