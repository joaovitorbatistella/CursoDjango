from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=150, blank=False, null=False)
    class Meta:
        verbose_name_plural = 'Autores'
    def __str__(self):
        return self.nome
    

class Livro(models.Model):
    CATEGORIA_CHOICES = {
        (1, 'Terror'),
        (2, 'Romance'),
        (3, 'Fantasia'),
    }
    categoria = models.IntegerField(choices=CATEGORIA_CHOICES)
    data_publicacao = models.DateField(null=False, blank=False)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    isbn = models.IntegerField(blank=False, null=False)
    autor = models.ForeignKey(Autor, related_name= 'livros', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo# + "-" + self.autor

    