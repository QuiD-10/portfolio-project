from django.db import models

# Create your models here.
#title
#publish data
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pubDate = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=3000)


#add to the admin