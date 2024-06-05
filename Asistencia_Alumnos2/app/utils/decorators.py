from django.shortcuts import render, redirect

def verificar_permisos():

    def deco_verificar_permisos(f):
        def check(request, *arg, **kwargs):
            if not request.user.es_profesor and not request.user.es_admin:
                return redirect("error_permisos")
            return f(request, *arg, **kwargs)

        return check

    return deco_verificar_permisos