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
