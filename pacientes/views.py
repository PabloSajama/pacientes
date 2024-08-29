from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import pacie
from .forms import pacienteForm

def lista_paciente(request):
    pacientes = pacie.objects.all()
    return render(request,'pacientes/lista_paciente.html',{'paciente': pacientes})

def detalle_paciente(request, pk):
    pacientes = get_object_or_404(pacientes, pk=pk)
    return render(request,'pacientes/detalle_paciente.html', {'paciente': pacientes})

def nuevo_paciente(request):
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_paciente')
    else:
        form = pacienteForm()
    return render(request,'pacientes/form_pacientes.html', {'form': form})

def editar_paciente(request, pk):
    paciente = get_object_or_404(paciente, pk=pk)
    if request.method == 'POST':
        form = pacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = pacienteForm(instance=paciente)
    return render(request, 'pacientes/form_pacientes.html', {'form': form})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/eliminar_paciente.html', {'paciente': paciente})