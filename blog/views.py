from django.shortcuts import redirect,render, get_object_or_404
from .models import Cancha,Alquiler
from .forms import ReservaForm

def ista_canchas(request):
	canchas = Cancha.objects.all()
	return render(request, 'blog/index.html', {'canchas': canchas})

def detalle_cancha(request,pk):
	cancha = get_object_or_404(Cancha, pk=pk)
	alquiler = cancha.alquileres.all()[:20]
	return render(request, 'blog/detalle_cancha.html', {'cancha': cancha ,'alquiler': alquiler})

def crear_reserva(request,pk):
	if request.method == "POST":
		form = ReservaForm(request.POST)
		if form.is_valid():
			reserva = form.save(commit=False)
			reserva.save()
			return redirect('detalle_cancha', pk=pk)
	else:
		form = ReservaForm()
	return render(request, 'blog/editar_reserva.html', {'form': form})

def editar_reserva(request, pk):
	alquiler = get_object_or_404(Alquiler, pk=pk)
	if request.method == "POST":
		form = ReservaForm(request.POST, instance=alquiler)
		if form.is_valid():
			alquiler.save()
			return redirect('editar_reserva', pk=pk)
	else:
		form = ReservaForm()
	form = ReservaForm(initial={'cancha': alquiler.cancha,'cliente': alquiler.cliente,'empleado': alquiler.empleado,'fechaReserva':alquiler.fechaReserva,'fechaHora':alquiler.fechaHora })
	return render(request, 'blog/editar_reserva.html', {'form': form,'alquiler': alquiler})

def borrar(request,pk):
	alquiler = get_object_or_404(Alquiler, pk=pk)
	alquiler.delete()
	cancha = get_object_or_404(Cancha, pk=alquiler.cancha.pk)
	alquileres = cancha.alquileres.all()[:20]
	return render(request, 'blog/detalle_cancha.html', {'cancha': cancha ,'alquileres': alquileres})
