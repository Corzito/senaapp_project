from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz

def home(request):
    """Vista para la página de inicio"""
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aprendices(request):
    """Vista para mostrar la lista de aprendices"""
    lista_aprendices = Aprendiz.objects.all().order_by('nombre', 'apellido')
    
    # Calcular estadísticas básicas
    total_aprendices = lista_aprendices.count()
    programas_count = Aprendiz.objects.values('programa').distinct().count()
    ciudades_count = Aprendiz.objects.values('ciudad').distinct().count()
    
    template = loader.get_template('lista_aprendices.html') 
    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': total_aprendices,
        'programas_count': programas_count,
        'ciudades_count': ciudades_count,
    }
    return HttpResponse(template.render(context, request))
