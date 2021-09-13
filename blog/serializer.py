from rest_framework import serializers

from .models import User, Entry

# データの形式をシリアライズする(sqliteのわけわからん型からJSONなどにパースする)
# コンピュータで実行中のプログラムがメインメモリ上に展開しているオブジェクトなどを、
# 一定のデータ形式や変換規則に従って文字列やバイト列に変換し、保存したり送受信できるようにすること

class UserSerializer(serializers.ModelSerializer):# 特定のmodelを指定すると、modelのフィールド設定が、Serializerのフィールド設定として暗黙的に実装される
    class Meta:
        model = User
        fields = ('id','name', 'mail') # idを追加してあげるとより親切


class EntrySerializer(serializers.ModelSerializer):
    
    #authorのserializerを上書き。なければauthor:1とIDしか書いてないのでわかりずらい。{"name":"Yuto","mail":"ichihara@arara.com"}がidの代わりに入るよになる
    # author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('article_id', 'title', 'body', 'created_at', 'status', 'author')