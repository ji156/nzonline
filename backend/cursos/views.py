from rest_framework import viewsets
from .serialize import CursosSerializer
from .models import Cursos


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer
