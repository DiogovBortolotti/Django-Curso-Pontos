
from rest_framework.viewsets import ModelViewSet

from atracoes.models import Atracao

from .serializers import AtracaoSerializer


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filterset_fields = ('nome', 'descricao')

    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'] na config #pip install django-filter
