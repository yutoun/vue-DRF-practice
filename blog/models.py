
from django.db import models
# SQLiteのDBスキーマを定義

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField() # 自動でメールアドレスのチェックを行う


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()# テキストになっているかチェック
    created_at = models.DateTimeField(auto_now_add=True) # dateになっているかチェック
    updated_at = models.DateTimeField(auto_now=True)# dateになっているかチェック
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE) # userfieldから取得, 関係するentriesが消されたら自動で消える指定