from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from project_api.models import UserItem
from django.core import serializers


# Create your views here.

class userItem(APIView):

    def get(self, request, format=None):

        an_apiview = serializers.serialize('json', UserItem.objects.all(), fields = ('id', 'name', 'img', 'status_text'))

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
