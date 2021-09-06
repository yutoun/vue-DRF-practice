from rest_framework import serializers

from .models import User, Entry

# データの形式をシリアライズする(sqliteのわけわからん型からJSONなどにパースする)
# コンピュータで実行中のプログラムがメインメモリ上に展開しているオブジェクトなどを、
# 一定のデータ形式や変換規則に従って文字列やバイト列に変換し、保存したり送受信できるようにすること

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')