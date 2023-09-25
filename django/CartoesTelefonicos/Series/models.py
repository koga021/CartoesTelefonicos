from django.db import models

# Create your models here.

class Series(models.Model):
    nome_serie = models.CharField(max_length=200,null=False)
    ano_lancamento = models.DateField(null=False)
    quantidade_cartoes = models.IntegerField(max_length=3,null=False)
    #pub_date = models.DateTimeField("date published")
    
    def __str__(self):
       return(self.nome_serie)
    
    


class Cartao(models.Model):
    identificador = models.ForeignKey(Series, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    tiragem = models.IntegerField(max_length=10,null=False)
    ordem = models.IntegerField(max_length=10,null=False)
    pub_date = models.DateTimeField("date published")



