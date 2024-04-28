"""
firstprojectのURLルーティングから呼び出し
"""
from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'blog'

# URLパターンを登録するための変数
# リクエストされたURLのページへのフルパス部分が''にマッチングした場合
# viewsモジュールのIndexViewクラスをインスタンス化する
# そのインスタンスのas_view()メソッドを呼び出す
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
