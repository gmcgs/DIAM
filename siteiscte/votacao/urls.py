from django.urls import include, path
from . import views

# (. significa que importa views da mesma directoria)
app_name = 'votacao'
urlpatterns = [
    # ex: votacao/
    path("", views.index, name='index'),
    # ex:
    path('criarquestao', views.criarquestao, name='criarquestao'),
    # ex: votacao/1
    path("<int:questao_id>", views.detalhe, name='detalhe'),

    path('save-value', views.save_value, name='save_value'),

    # ex:votacao/3/resultados
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    # ex: votacao/5/voto
    path('<int:questao_id>/voto', views.voto, name='voto'),

    path('<int:questao_id>/criaropcao', views.criaropcao, name='criaropcao'),

    path('<int:questao_id>/save_option', views.save_option, name='save_option'),
]
