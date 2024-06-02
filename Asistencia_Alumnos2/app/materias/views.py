from django.views.generic.list import ListView

from .models import Materia

class Listar(ListView):
    template_name='materias/listar.html'
    model = Materia
    context_object_name = 'materias'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by("nombre")

