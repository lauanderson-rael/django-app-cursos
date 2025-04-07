from django.db import models

# Create your models here.
class Curso(models.Model):
   nome = models.CharField(max_length=50)
   carga_horaria = models.IntegerField()
   data_criacao = models.DateTimeField()
   ativo = models.BooleanField(default=True)

   # magica do python
   def __str__(self):
      return self.nome
