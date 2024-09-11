from django.shortcuts import render, redirect
from .models import Vuelo
from .forms import VueloForm
from django.db.models import Avg

def inicio(request):
    return render(request, 'inicio.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
    else:
        form = VueloForm()
    return render(request, 'registrar_vuelo.html', {'form': form})

def listar_vuelos(request):
    vuelos = Vuelo.objects.all().order_by('precio')
    return render(request, 'listar_vuelos.html', {'vuelos': vuelos})

def estadisticas_vuelos(request):
    nacionales = Vuelo.objects.filter(tipo='N').count()
    internacionales = Vuelo.objects.filter(tipo='I').count()
    promedio_nacionales = Vuelo.objects.filter(tipo='N').aggregate(Avg('precio'))['precio__avg']
    
    return render(request, 'estadisticas_vuelos.html', {
        'nacionales': nacionales,
        'internacionales': internacionales,
        'promedio_nacionales': promedio_nacionales,
    })
