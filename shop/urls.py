from django.urls import path
from .views import greetings, ListItem, DetailItem

urlpatterns = [
    path('shop/greetings', greetings, name='greetings'),
    path('shop/', ListItem.as_view(), name='list_item'),
    path('shop/<int:pk>', DetailItem.as_view(), name='detail_item')
]