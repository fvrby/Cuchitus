from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Cliente, Post
from django.shortcuts import redirect

# PARA INICIO DE SESION
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    Cliente = Cliente.objects.order_by('rut')
    return render(request, 'Cuchitus/index.html', {'Cliente': Cliente})

def Productos(request):
    Post = Post.objects.order_by('nombre')
    return render(request, 'Cuchitus/Productos.html', {'Post': Post})