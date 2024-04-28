from django.shortcuts import render

from django.views.generic.base import TemplateView

# クラスのパターン
class IndexView(TemplateView):
    '''トップページのビュー
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name (str): レンダリングするテンプレートのパス
    '''
    template_name = 'index.html'

# 関数のパターン
def about(request):
    '''アバウトのビュー
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name (str): レンダリングするテンプレートのパス
    '''
    return render(request, 'about.html')

def post(request):
    '''postのビュー
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name (str): レンダリングするテンプレートのパス
    '''
    return render(request, 'post.html')

def contact(request):
    '''アバウトのビュー
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name (str): レンダリングするテンプレートのパス
    '''
    return render(request, 'contact.html')