from rest_framework import routers
from .views import UserViewSet, EntryViewSet

# このurls.pyにじゃないとblog app内のルーティングができないため、一旦このurls.pyにルーティングする必要がある
# この段階までがルーティング。views.pyから見える部分

router = routers.DefaultRouter() # リクエストのHTTPメソッドとエンドポイントを判別し、対応するViewSetのアクションを実行する
router.register('users', UserViewSet) # api/usersでUserViewSetを呼び出す
router.register('entries', EntryViewSet) # api/entriesでentryViewSetを呼び出す