from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Questao, Opcao


def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


def criarquestao(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/criarquestao.html', context)

def detalhe(request, questao_id):
    questao = Questao.objects.get(pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})

def save_value(request):
    if request.method == 'POST':
        my_model = Questao(questao_texto=request.POST['texto'], pub_data=timezone.now())
        my_model.save()
        return HttpResponseRedirect(reverse('votacao:index'))


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})


def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', {
            'questao': questao,
            'error_message': "Não escolheu uma opção",
        })
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
        # Retorne sempre HttpResponseRedirect depois de tratar os dados POST de um form
        # pois isso impede os dados de serem tratados repetidamente se o utilizador
        # voltar para a página web anterior.
        return HttpResponseRedirect(
            reverse('votacao:resultados', args=(questao.id,))
        )


def criaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/criaropcao.html', {'questao': questao})


def save_option(request, questao_id):
    if request.method == 'POST':
        q = Questao.objects.get(pk=questao_id)
        q.opcao_set.create(opcao_texto=request.POST['texto'], votos=0)
        return HttpResponseRedirect(reverse('votacao:index'))
