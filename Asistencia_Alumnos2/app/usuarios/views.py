from django.shortcuts import render

from app.usuarios.models import Usuario

def listar_usuarios(request):
    template_name = 'usuarios/listar_todos.html'
    lista_usuarios = Usuario.objects.all()

    #print("--->", lista_usuarios)
    #print("interando usuarios")
    #print("QUERY:", lista_usuarios.query)

    #for us in lista_usuarios:
    #    print("USUARIOS:", us)

    ctx = {
        'usuarios': lista_usuarios,
        #'fecha_hora': '29/04/2024 15:28 hs'
    }
    return render(request, template_name, ctx)
