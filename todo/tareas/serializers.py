from rest_framework import serializers

from .models import Tarea

class TareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id', 'descripcion','estado','adjunto')