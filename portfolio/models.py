from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=20, default="O que deseja saber?")
    nome_autor = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo[:10]

class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=20)
    pontos = models.IntegerField(max_length=20, default=0)

    def __str__(self):
        return self.nome[:10]


class Professor(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome[:10]


class Linguagem(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome[:10]


class Projeto(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome[:10]


class Cadeira(models.Model):
   nome = models.CharField(max_length=20)
   ano = models.IntegerField()
   descricao = models.TextField()
   linguagens = models.ManyToManyField(Linguagem)
   docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
   docentes_praticas = models.ManyToManyField(Professor, related_name='cadeiras')
   projetos = models.ManyToManyField(Projeto)

   def __str__(self):
       return self.nome[:10]
