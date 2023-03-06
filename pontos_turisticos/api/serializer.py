
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer
from comentarios.api.serializer import ComentarioSerializer
from enderecos.api.serializer import EnderecoSerializer
from pontos_turisticos.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    # Tras todo os registros relacionados somente a ele então não tem many
    endereco = EnderecoSerializer()
    # Tras todo os registros relacionados de um pra muito devido o many
    atracoes = AtracaoSerializer(many=True)
    comentario = ComentarioSerializer(many=True)
    avaliacoes = AvaliacoesSerializer(many=True)

    # cria se uma novo campo no   serializer
    descricao_completa = SerializerMethodField()
    descricao_completa2 = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = '__all__'

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'

    def get_descricao_completa2(self, obj):
        return obj.descricao_completa2
