from django.contrib.auth.models import User
from rest_framework import serializers
from list.models import Item, List, Pledge
import stripe


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):

        user = User.objects.create_user(email=validated_data['email'], username=validated_data['username'],
                                        password=validated_data['password'])
        return user


class PledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pledge
        fields = ('id', 'user', 'item', 'amount')
    #
    # def create(self, validated_data):
    #     pledge = Pledge.objects.create(**validated_data)
    #     try:
    #         charge = stripe.Charge.create(
    #             amount=self.amount,
    #             currency="usd",
    #             source=validated_data["token"],
    #             description="Pledge"
    #         )
    #         return pledge
    #     except stripe.error.CardError:
    #         return




class ItemSerializer(serializers.ModelSerializer):
    reserved = serializers.ReadOnlyField()
    pledge_set = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description', 'image', 'list', 'item_link', 'reserved', 'pledge_set')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    item_set = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ('id', 'title', 'user', 'posted_at', 'item_set', 'price')

