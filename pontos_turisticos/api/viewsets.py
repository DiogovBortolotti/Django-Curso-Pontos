from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.api.serializer import PontoTuristicoSerializer
from pontos_turisticos.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    # cuidar pois da dor de cabeça para ajustar
    authentication_classes = [TokenAuthentication]

    # cuidar pois da dor de cabeça para ajustar
    permission_classes = (DjangoModelPermissions,)  # IsAuthenticated

   # queryset = PontoTuristico.objects.all() # daria para alterar  o.filter(aprovado=True) so que não e o melhor forma
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ('nome', 'descricao')
    # so pode o valor que seje unico exemplo cpf e tals pq não pode retornar outro que ha mas de 1 registro
    lookup_field = 'nome'
    # so que assim permite eu fazer outras filtragens

    def get_queryset(self):
        id = self.request.query_params.get('id')
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()  # Pre - Loader

        # Filtros
        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(
                nome__iexact=nome)  # tira o senstive dele adicionando __iexact
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
       # return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        # return Response({'test': 1234}) # testa estatico
        # return Response(PontoTuristico.objects.all())
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
