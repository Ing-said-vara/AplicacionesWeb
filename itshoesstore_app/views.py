from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def agregar_producto(request): 
    if request.method == 'POST':
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})

