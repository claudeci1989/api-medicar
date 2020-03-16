from rest_framework.serializers import ModelSerializer, RelatedField
from gerenciamento.models import Especialidades, Medicos, Horarios, Agenda
from rest_framework.validators import UniqueTogetherValidator

class EspecialidadesSerializer(ModelSerializer):
    class Meta:
        model = Especialidades
        fields = ['id','nome']

class MedicosSerializer(ModelSerializer):
    especialidade = EspecialidadesSerializer(read_only=True)

    class Meta:
        model = Medicos
        fields = ['id','nome','crm','especialidade']

class HorariosSerializer(ModelSerializer):
    class Meta:
        model = Horarios
        fields = ['hora']

class AgendaSerializer(ModelSerializer):
    medico = MedicosSerializer(many=True)
    horarios = HorariosSerializer(many=True)

    class Meta:
        model = Agenda
        fields = ['id','medico','dia','horarios']