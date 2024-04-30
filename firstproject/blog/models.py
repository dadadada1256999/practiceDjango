from django.db import models

# モデル
class BlogPost(models.Model):
    # カテゴリに設定する項目を入れこのタプルとして定義
    # 最初の要素はモデルが使用する値、2番目の要素は選択メニューに表示する文字列
    CATEGORY = (('science', '科学のこと'), ('dailylife', '日常のこと'), ('music', '音楽のこと'))

    # varcharのカラム
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    # textのカラム
    content = models.TextField(
        verbose_name="本文"
    )

    # datetimeのカラム
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    # Selectボックス
    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        # 選択肢を指定
        choices=CATEGORY
    )

    def __str__(self) -> str:
        return self.title;

