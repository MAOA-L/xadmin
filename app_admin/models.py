from django.db import models


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=36, unique=True, db_index=True)
    gmt_create = models.DateTimeField(auto_now_add=True)
    gmt_modified = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    text = models.TextField()
    sort = models.CharField(max_length=255)
    label = models.CharField(max_length=255, null=True)
    see_number = models.IntegerField(null=True)
    comment_number = models.IntegerField(null=True)

    class Meta:
        db_table = 'article'


class Sort(models.Model):
    """分类"""
    gmt_create = models.DateTimeField(auto_now_add=True)
    gmt_modified = models.DateTimeField(auto_now=True)
    # 分类编号
    sort_feature = models.CharField(max_length=240, unique=True, verbose_name="类别编号")
    # 分类名称
    sort_name = models.CharField(max_length=255, verbose_name="类别名称")

    def __str__(self):
        return self.sort_name

    class Meta:
        db_table = "sort"
        verbose_name_plural = verbose_name = "文章分类"
