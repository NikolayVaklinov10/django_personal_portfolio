from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()  # it allows more text to be enter than CharField this is the reason for picking it
    image = models.ImageField(upload_to='images/')
