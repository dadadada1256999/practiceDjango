"""
ルーティング用のファイル
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 下記に追加していく
    path('', include('blog.urls'))
]
