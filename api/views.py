
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from api.serializers import UserSerializer, ListSerializer, ItemSerializer, PledgeSerializer
from list.models import List, Item, Pledge
import stripe


class SmallPagination(PageNumberPagination):
    page_size = 10


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class ListCreateList(generics.ListCreateAPIView):
    queryset = List.objects.order_by('posted_at')
    serializer_class = ListSerializer
    pagination_class = SmallPagination

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class DetailUpdateList(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListCreateItem(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailUpdateItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ListCreatePledge(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    # def perform_create(self, serializer):
    #     stripe.api_key = STRIPE_API_KEY
    #     token =
