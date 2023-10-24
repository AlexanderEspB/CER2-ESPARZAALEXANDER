from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad,Comunicado

# Create your views here.
def index(request):
    entidades=Entidad.objects.all()
    entidad_filtrada=None
    comunicado=Comunicado.objects.filter(visible=True).order_by('-fecha_publicacion')

    if 'entidad' in request.GET:
        entidad_id =request.GET['entidad']
        if entidad_id:
            comunicado= Comunicado.objects.filtrer(entidad_id=entidad_id,visible=True).order_by('-fecha_publicacion')
            entidad_filtrada=Entidad.objects.get(id=entidad_id)
    
    Informacion = {
    'entidades': entidades,
    'comunicado': comunicado,
    'entidad_filtrada': entidad_filtrada,
}

    return render(request,'myapp/index.html',Informacion)

