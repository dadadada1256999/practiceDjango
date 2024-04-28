from django.shortcuts import render

from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    '''トップページのビュー
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name (str): レンダリングするテンプレートのパス
    '''
    template_name = 'index.html'