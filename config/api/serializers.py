
from django.db import models
from .models import SuperMarket 
from rest_framework import serializers

class SuperMarketSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SuperMarket
        fields = ('id', 'name', 'product', 'price',)