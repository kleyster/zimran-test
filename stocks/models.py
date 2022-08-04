from django.db import models


class News(models.Model):

    id = models.IntegerField(primary_key=True)
    related = models.CharField(max_length=15)
    posted_at = models.DateTimeField()
    headline = models.TextField()
    source = models.CharField(max_length=50)
    summary = models.TextField(null=True)
    url = models.URLField()

class NewsImages(models.Model):

    image = models.URLField()
    news = models.ForeignKey("stocks.News",related_name="images",on_delete=models.CASCADE)