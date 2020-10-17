from rest_framework import serializers
from numbers_app.models import NumberSort


class SerializerInput(serializers.Serializer):
    items = serializers.ListField()


class NumberSortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberSort
        fields = '__all__'
