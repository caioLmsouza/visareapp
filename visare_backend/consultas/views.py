from django.http import JsonResponse
from .models import Consulta

def agenda_consultas(request):
    # Filtros podem ser aplicados aqui usando request.GET
    eventos = []
    consultas = Consulta.objects.all().order_by('data_hora_inicio')
    for idx, consulta in enumerate(consultas, start=1):
        eventos.append({
            "id": consulta.id,
            "title": f"{idx}ª - {consulta.paciente.nome} - {consulta.profissional.nome}",
            "start": consulta.data_hora_inicio.isoformat(),
            "end": consulta.data_hora_fim.isoformat(),
            "color": "#ef87b8"  # Exemplo, pode ser dinâmico por status/urgência
        })
    return JsonResponse(eventos, safe=False) 