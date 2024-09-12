from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Tarefa, TarefaTodos


class UserSerializer(serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class TarefaSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'atribuicao',  ]
        
class TarefaTodosSerializer(serializers.ModelSerializer ):
    class Meta:
        model = TarefaTodos
        fields = ['nome', 'descricao', ]
