from django.conf.urls import url, include
from django.contrib import admin

from blog.urls import router as blog_router

urlpatterns = [
    url('admin/', admin.site.urls),
    # blog.urlsをincludeする
    url('api/', include(blog_router.urls)), # 保存したらすぐブラウザに反映される←apiのurl変更したりしたらすぐ繋がらなくなる.blog/urls.pyを上でimportしている
]