from django.contrib.auth.models import User
from rest_framework import serializers
from list.models import Item, List


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'list_set')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    item_set = serializers.HyperlinkedRelatedField(many=True, queryset=Item.objects.all(),
                                                   view_name='api_item_detail_update')

    class Meta:
        model = List
        fields = ('title', 'user', 'posted_at', 'item_set', 'price')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'image', 'list')