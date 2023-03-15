
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from avaliacoes.api.serializers import AvaliacoesSerializer
from comentarios.api.serializer import ComentarioSerializer
from enderecos.api.serializer import EnderecoSerializer
from enderecos.models import Endereco
from pontos_turisticos.models import DocIdentificacao, PontoTuristico


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

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        avaliacoes = validated_data['avaliacoes']
        del validated_data['avaliacoes']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        ponto.avaliacoes.set(avaliacoes)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto
