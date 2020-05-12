from django.db import models

# Create your models here.

class Tarea(models.Model):

    id          = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45) 
    estado      = models.BooleanField(default=False)
    adjunto     = models.FileField(blank=True, null=True, upload_to='images/')
    
    def __str__(self):
        return '{}'.format(self.id)


