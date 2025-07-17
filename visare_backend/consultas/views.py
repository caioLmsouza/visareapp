from django.http import JsonResponse
from .models import Consulta

def agenda_consultas(request):
    # Filtros podem ser aplicados aqui usando request.GET
    eventos = []
    for consulta in Consulta.objects.all():
        eventos.append({
            "id": consulta.id,
            "title": f"{consulta.paciente.nome} - {consulta.profissional.nome}",
            "start": consulta.data_hora_inicio.isoformat(),
            "end": consulta.data_hora_fim.isoformat(),
            "color": "#ef87b8"  # Exemplo, pode ser dinâmico por status/urgência
        })
    return JsonResponse(eventos, safe=False) 