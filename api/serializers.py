from rest_framework import serializers
from .models import Shop,Person,Online

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class OnlineSerializer(serializers.ModelSerializer):
    class Meta :
        model = Online
        fields = '__all__'