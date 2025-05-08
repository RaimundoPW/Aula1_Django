from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_tarefas, name="lista_tarefas"),
    path("tarefa/<int:id>", views.tarefaView, name="tarefa-view")
    

]
