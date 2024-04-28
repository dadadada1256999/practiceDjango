"""
firstprojectのURLルーティングから呼び出し
"""
from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
# {% url 'blog:contact' %}でindex.htmlから呼び出したとき、app_name:urlpatternsでマッチングする
app_name = 'blog'

# URLパターンを登録するための変数
# リクエストされたURLのページへのフルパス部分が''にマッチングした場合
# viewsモジュールのIndexViewクラスをインスタンス化する
# そのインスタンスのas_view()メソッドを呼び出す
urlpatterns = [
    # クラスのパターン
    path('', views.IndexView.as_view(), name='index'),
    # 関数のパターン
    path('about', views.about, name='about'),
    path('post', views.post, name='post'),
    path('contact', views.contact, name='contact')
]
