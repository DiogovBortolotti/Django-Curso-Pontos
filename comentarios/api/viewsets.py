from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializer import ComentarioSerializer
from comentarios.models import Comentario


class ComentarioViewset(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
