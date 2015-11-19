from django.contrib.auth.models import User
from rest_framework import serializers
from list.models import Item, List, Pledge


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):

        user = User.objects.create_user(email=validated_data['email'], username=validated_data['username'],
                                        password=validated_data['password'])
        return user


class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    item_set = serializers.HyperlinkedRelatedField(many=True, queryset=Item.objects.all(),
                                                   view_name='api_item_detail_update')

    class Meta:
        model = List
        fields = ('title', 'user', 'posted_at', 'item_set', 'price')


class PledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pledge
        fields = ('user', 'item', 'amount')


class ItemSerializer(serializers.ModelSerializer):
    reserved = serializers.ReadOnlyField()
    pledge_set = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'image', 'list', 'item_link', 'reserved', 'pledge_set')