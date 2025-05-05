from django.shortcuts import render

# Create your views here.
def lista_tarefas(request):
    return render(request, "tarefas/list.html")