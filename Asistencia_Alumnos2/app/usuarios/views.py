
from django.shortcuts import render
from django.views.generic.list import ListView

from django_filters.views import FilterView

from app.usuarios.models import Usuario

from .filterset import UsuarioFilter

def listar_usuarios(request):
    template_name = 'usuarios/listar_todos.html'
    lista_usuarios = Usuario.objects.all().order_by("id")

    #print("--->", lista_usuarios)
    #print("interando usuarios")
    #print("QUERY:", lista_usuarios.query)

    #for us in lista_usuarios:
    #    print("USUARIOS:", us)

    ctx = {
        'usuarios': lista_usuarios,
        'icono': "o"
        #'fecha_hora': '29/04/2024 15:28 hs'
    }
    return render(request, template_name, ctx)

class ListarUsuarios(FilterView):
    template_name ='usuarios/listar_todos.html'
    model = Usuario
    context_object_name = 'usuarios'
    paginate_by = 20
    filterset_class=UsuarioFilter

    def get_context_data(self, **kwargs):
        ctx = super(ListarUsuarios, self).get_context_data(**kwargs)
        ctx["icono"] = "o"

        return ctx
    def get_queryset(self):
        return self.model.objects.all().order_by("last_name", "first_name")
