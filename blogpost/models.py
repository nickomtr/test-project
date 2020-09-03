from django.db import models

class PostText(models.Model):
    post_image = models.ImageField(upload_to = 'event_media/')
    post_text = models.CharField(max_length=300)
    post_date = models.DateTimeField()
    post_title =  models.CharField(max_length=10)
