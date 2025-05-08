from django.shortcuts import render, get_object_or_404 
from .models import Tarefas

# Create your views here.
def lista_tarefas(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')

    return render(request, "tarefas/list.html", {"tarefas":tarefas_list})

def tarefaView(request, id):
    taefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':taefa })