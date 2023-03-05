from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    # DBのスキーマを定義する
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)

    # DBの管理パネルをわかりやすく表示されるようにする
    # これがあると、一覧表示した時にtitleが見出しになる
    def __str__(self):
        return self.title

        class Meta:
            # 並べ替えたい要素を指定する
            ordering = ["completed"]
