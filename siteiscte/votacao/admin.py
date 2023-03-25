from django.contrib import admin

# Register your models here.
from .models import Questao, Opcao, Aluno

admin.site.register(Questao)
admin.site.register(Opcao)
admin.site.register(Aluno)