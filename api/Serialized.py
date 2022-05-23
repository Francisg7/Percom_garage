
from PercomGarage.models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class ClientSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    voiture = 'VoitureSerializer()'
    facture = 'FactureSerializer()'

    class Meta:
        model = Client
        fields = '__all__'


class CommandeSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    client = "ClientSerializer()"
    employer ="EmployeSerializer()"
    stocks = "StockSerializer(many=True, read_only=True)"

    class Meta:
        model = Commande
        fields = '__all__'

    extra_kwargs={'stocks': {'required': False}}


class EmployeSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    garage = 'GarageSerializer()'

    class Meta:
        model = Employe
        fields = '__all__'


class FactureSerializer( WritableNestedModelSerializer,serializers.ModelSerializer):
    client = 'ClientSerializer(many=True, read_only=True)'
    employer = 'EmployeSerializer()'

    class Meta:
        model = Facturation
        fields = '__all__'
    extra_kwargs={'client': {'required': False}}


class GarageSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    employer = 'EmployeSerializer(null=True)'
    vehicule = 'VoitureSerializer(many=True, read_only=True)'

    class Meta:
        model = Garage
        fields = '__all__'
    extra_kwargs = {'vehicule': {'required': False}}


class InterventionSerializer( WritableNestedModelSerializer,serializers.ModelSerializer):
    employer = 'EmployeSerializer(many = True, read_only=True)'
    client = 'ClientSerializer()'
    vehicule = 'VoitureSerializer(many=True, read_only=True)'

    class Meta:
        model = Intervention
        fields = '__all__'
    extra_kwargs = {'employer': {'required': False}}
    extra_kwargs = {'vehicule': {'required': False}}


class LaverieSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    employer = 'EmployeSerializer()'
    vehicule = 'VoitureSerializer(many=True, read_only=True)'

    class Meta:
        model = Laverie
        fields = '__all__'
    extra_kwargs = {'vehicule': {'required': False}}


class LocationSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    client = 'ClientSerializer(many=True, read_only=True)'
    vehicule = 'VoitureSerializer(many=True, read_only=True)'

    class Meta:
        model = Locations
        fields = '__all__'
    extra_kwargs = {'vehicule': {'required': False}}
    extra_kwargs = {'client': {'required': False}}


class RendezVousSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    client = 'ClientSerializer(many=True, read_only=True)'

    class Meta:
        model = RendezVous
        fields = '__all__'
    extra_kwargs = {'client': {'required': False}}


class PieceSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class StockSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    employer = 'EmployeSerializer(many=True, read_only=True)'
    piece = 'PieceSerializer(many=True, read_only=True)'

    class Meta:
        model = Stock
        fields = '__all__'
    extra_kwargs = {'employer': {'required': False}}
    extra_kwargs = {'piece': {'required': False}}


class VoitureSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    clients = 'ClientSerializer()'

    class Meta:
        model = Vehicules
        fields = '__all__'


class UserCreateSerializer( WritableNestedModelSerializer,UserCreateSerializer,):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name','last_name','username', 'cpassword', 'password', 'phone')

