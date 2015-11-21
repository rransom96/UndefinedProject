from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from list.models import List, Item, Pledge
from rest_framework import status
from rest_framework.test import APITestCase


class ListTests(APITestCase):
    image = 'http://www.dumpaday.com/wp-content/uploads/2012/07/funny-baby1.jpg'
    item_link = '''http://www.ebay.com/itm/A-Box-Of-Nothing-
    /272026445769?hash=item3f560a27c9:g:tCQAAOSwI-BWLIPi'''

    def setUp(self):
        self.user1 = User.objects.create_user(username='undefined',
                                              email='undefined@tests.com',
                                              password='tests')
        self.list1 = List.objects.create(title='undefined list',
                                         user=self.user1)
        self.item1 = Item.objects.create(name='undefined item',
                                         price=999999999.99,
                                         description='undefined description',
                                         image=self.image, list=self.list1,
                                         item_link=self.item_link)
        self.pledge1 = Pledge.objects.create(user=self.user1, item=self.item1,
                                             amount=999999999.99)

    def test_list_list(self):
        url = reverse('api_list_list_create')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_list = response.data['results'][0]
        self.assertEqual(response_list['title'], self.list1.title)

    def test_create_list(self):
        url = reverse('api_list_list_create')
        data = {'title': 'test'}
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(List.objects.count(), 1)
        self.assertEqual(self.user1.id, response.data['user'])


class ItemTests(APITestCase):
    image = 'http://www.dumpaday.com/wp-content/uploads/2012/07/funny-baby1.jpg'
    item_link = '''http://www.ebay.com/itm/A-Box-Of-Nothing-
    /272026445769?hash=item3f560a27c9:g:tCQAAOSwI-BWLIPi'''

    def setUp(self):
        self.user1 = User.objects.create_user(username='undefined',
                                              email='undefined@tests.com',
                                              password='tests')
        self.list1 = List.objects.create(title='undefined list',
                                         user=self.user1)
        self.item1 = Item.objects.create(name='undefined item',
                                         price=999999999.99,
                                         description='undefined description',
                                         image=self.image, list=self.list1,
                                         item_link=self.item_link)
        self.pledge1 = Pledge.objects.create(user=self.user1, item=self.item1,
                                             amount=999999999.99)

    def test_list_item(self):
        url = reverse('api_item_list_create')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_item = response.data['results'][0]
        self.assertEqual(response_item['name'], self.item1.name)

    def test_create_item(self):
        url = reverse('api_item_list_create')
        data = {'name' : 'test item', 'price': 100.10,
                'description': 'undefined description', 'image': self.image,
                'item_link': self.item_link}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)


class PledgeTests(APITestCase):
    image = 'http://www.dumpaday.com/wp-content/uploads/2012/07/funny-baby1.jpg'
    item_link = '''http://www.ebay.com/itm/A-Box-Of-Nothing-
    /272026445769?hash=item3f560a27c9:g:tCQAAOSwI-BWLIPi'''

    def setUp(self):
        self.user1 = User.objects.create_user(username='undefined',
                                              email='undefined@tests.com',
                                              password='tests')
        self.user2 = User.objects.create_user(username='undefined1',
                                              email='undefined2@tests.com',
                                              password='tests3')
        self.list1 = List.objects.create(title='undefined list',
                                         user=self.user1)
        self.item1 = Item.objects.create(name='undefined item',
                                         price=999999999.99,
                                         description='undefined description',
                                         image=self.image, list=self.list1,
                                         item_link=self.item_link)
        self.pledge1 = Pledge.objects.create(user=self.user1, item=self.item1,
                                             amount=999999999.99)

    def test_list_pledge(self):
        url = reverse('api_pledge_list_create')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        response_list = response.data['results'][0]
        self.assertEqual(response_list['user'], self.user2)

    def test_create_item(self):
        url = reverse('api_item_list_create')
        data = {'user': self.user2, 'item': self.item1, 'amount': 10.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(self.user2.id, response.data['user'])