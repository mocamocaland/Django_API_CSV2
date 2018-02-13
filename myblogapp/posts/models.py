from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()


    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:50]


    def to_list(self):
        api_date = datetime.strftime(self.published, '%Y/%m/%d')
        return "{}, {}, {}".format(self.title, api_date, self.body)
            

    class Meta:
        db_table = "posts_post"
