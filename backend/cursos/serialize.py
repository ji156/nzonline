from rest_framework import serializers
from .models import Cursos


class CursosSerializer(serializers.ModelSerializer):
    # Define un campo personalizado para la URL de la imagen
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Cursos
        fields = '__all__'

    # Método para obtener la URL de la imagen
    def get_imagen_url(self, obj):
        # Asegúrate de utilizar el nombre del campo de tu modelo donde está la imagen
        if obj.imagen:
            return self.context['request'].build_absolute_uri(obj.imagen.url)
        return None
