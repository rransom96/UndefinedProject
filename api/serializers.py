from django.contrib.auth.models import User
from rest_framework import serializers
from list.models import Item, List, Pledge


class ShortListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ('id', 'title', 'posted_at', 'inactive')


class UserSerializer(serializers.ModelSerializer):
    list_set = ShortListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'list_set', 'pledge_set')

    def create(self, validated_data):

        user = User.objects.create_user(email=validated_data['email'],
                                        username=validated_data['username'],
                                        password=validated_data['password'])
        return user


class PledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pledge
        fields = ('id', 'user', 'item', 'amount', 'charge')

    def create(self, validated_data):
        pledge = Pledge.objects.create(user=validated_data['user'],
                                       item=validated_data['item'],
                                       amount=validated_data['amount'],
                                       charge=validated_data['charge_id'])
        return pledge


class ItemSerializer(serializers.ModelSerializer):
    reserved = serializers.ReadOnlyField()
    pledge_set = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description', 'image', 'list',
                  'item_link', 'reserved', 'pledge_set')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    inactive = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.id')
    item_set = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ('id', 'title', 'user', 'posted_at', 'item_set', 'price',
                  'deadline', 'inactive')
