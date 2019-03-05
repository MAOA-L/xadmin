from django.db import models


class Article(models.Model):
    id = models.BigIntegerField(primary_key=True, db_index=True)
    gmt_create = models.DateTimeField(auto_now_add=True)
    gmt_modified = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True)
    sort = models.CharField(max_length=255, null=True)
    label = models.CharField(max_length=255, null=True)
    see_number = models.IntegerField()
    comment_number = models.IntegerField()

    class Meta:
        db_table = 'article'
