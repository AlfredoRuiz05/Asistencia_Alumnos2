from django.shortcuts import render

def listar_clases(request):
    template_name = "clases/lista.html"
    ctx = {

    }
    return render(request, template_name, ctx)
