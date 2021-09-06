import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet): # modelviewsetを使うとreturnとかなしでいける
    queryset = User.objects.all() # userテーブルのオブジェクト全権取得
    serializer_class = UserSerializer # 先ほど指定したserializerを指定


class EntryViewSet(viewsets.ModelViewSet): # modelViewSet is to get the complete set of default read and write operations.
    queryset = Entry.objects.all() # Entryテーブルのオブジェクト全権取得
    serializer_class = EntrySerializer # userテーブルのオブジェクト全権取得