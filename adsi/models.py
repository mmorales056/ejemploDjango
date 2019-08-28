from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    identificacion = models.IntegerField()
    usuario = models.CharField(max_length=150, unique=True)
    clave = models.CharField(max_length=150)
    roles=(
        ('1','Aprendiz'),
        ('2', 'Vocero')       
    )
    rol = models.CharField(max_length=1, choices=roles, default='1')
    #métodos
    def __str__(self):
        return self.nombre

class Fichas(models.Model):
    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.DO_NOTHING)
    codigo = models.IntegerField()
    programa = models.CharField(max_length=254)
    def __str__(self):
        return self.codigo


