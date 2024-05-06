from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {})
def home(request):
    template_name = 'home.html'
    lista_alumnos = [
        {
            'nombre': 'lucas',
            'apellido': 'ibañes',
            'legajo': 123, 
            'habilitado': True
        },
        {
            'nombre': 'federico',
            'apellido': 'aguirre',
            'legajo': 222,
            'habilitado': False
        }
    ]

    ctx = {
        'alumnos': lista_alumnos,
        'fecha_hora': '29/04/2024 15:28 hs'
    }
    return render(request, template_name, ctx)