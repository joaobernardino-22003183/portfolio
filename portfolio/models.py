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
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return self.nome[:10]


class Professor(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome[:30]


class Linguagem(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome[:10]


class Projeto(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()
    imagem = models.ImageField(blank=True, upload_to='image')

    def __str__(self):
        return self.nome[:30]


class Cadeira(models.Model):
   nome = models.CharField(max_length=40)
   ano = models.IntegerField()
   ects = models.CharField(max_length=20)
   descricao = models.TextField()
   linguagens = models.ForeignKey(Linguagem, on_delete=models.CASCADE, default="linguagens")
   docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
   docentes_praticas = models.ForeignKey(Professor, related_name='cadeiras', on_delete=models.CASCADE,default="nome")
   projetos = models.ForeignKey(Projeto, on_delete=models.CASCADE, default="projetos")
   ranking = models.CharField(max_length=40)
   imagem = models.ImageField(blank= True, upload_to='image')

   def __str__(self):
       return self.nome[:30]

class TFC(models.Model):
    autor = models.CharField(max_length=200)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.IntegerField()
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(blank=True, upload_to='image')
    relatorio =  models.CharField(max_length=1000)
    link_github = models.CharField(max_length=1000)

    def __str__(self):
        return self.titulo[:70]