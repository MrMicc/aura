from django.db import models

# Create your models here.

#como herdamos um model não precisamos da funciton init
#ao final da alteração de um model é necessário rodar o makemigrations
#2 - Aplicar o schema no banco migrate
class Perfil(models.Model):

    nome = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=155, null=False)

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

