from django.conf.urls import url
from rest_framework.authtoken import views
from api.views import DetailUpdateList, ListCreateList, DetailUpdateItem, \
    ListCreateItem, ListCreateUsers, ListPledge
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^lists/(?P<pk>\d+)', DetailUpdateList.as_view(),
        name='api_list_detail_update'),
    url(r'^lists/', ListCreateList.as_view(), name='api_list_list_create'),
    url(r'^items/(?P<pk>\d+)', DetailUpdateItem.as_view(),
        name='api_item_detail_update'),
    url(r'^items/', ListCreateItem.as_view(), name='api_item_list_create'),
    url(r'^users/', ListCreateUsers.as_view(), name='api_user_list'),
    url(r'^pledges/', ListPledge.as_view(), name='api_pledge_list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)