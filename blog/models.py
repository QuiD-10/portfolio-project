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

    def summary(self):
        return self.body[:100]
    
    def pub_Date(self):
        return self.pubDate.strftime('%b %e, %Y')
    
    def __str__(self):
        return self.title

#add to the admin