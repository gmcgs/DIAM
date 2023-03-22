from votacao.models import Questao, Opcao
from django.db.models import Sum
from django.db.models import Max

def total_votos():
    total_votes = Opcao.objects.aggregate(Sum('votos'))
    return total_votes['votos__sum']


def opcao_com_mais_votos():
    questoes = []
    for questao in Questao.objects.all():
        opcao_mais_votada = questao.opcao_set.annotate(max_votos=Max('votos')).order_by('-max_votos').first()
        if opcao_mais_votada:
            questoes.append({
                'questao_texto': questao.questao_texto,
                'opcao_texto': opcao_mais_votada.opcao_texto,
                'votos': opcao_mais_votada.votos
            })
    return questoes
