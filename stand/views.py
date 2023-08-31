from django.shortcuts import get_object_or_404, redirect, render
from .models import Reserva
from .forms import ReservaForm

# Create your views here.
def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
        else:
            print(form.errors)
    else:
        form = ReservaForm()

    return render(request, 'stand/form.html', {'form': form})

def reserva_listar(request):
    reservas = Reserva.objects.all()
    return render(request, 'stand/index.html', {'reservas': reservas})

def detalhe_reserva(request,id):
    reserva = Reserva.objects.get(id=id)
    context = {
        'reserva':reserva
    }
    return render(request,'stand/detalhe.html',context)

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar') 