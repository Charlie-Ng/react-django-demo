from django.db import models

# Create your models here.
class UserItem(models.Model):

    name = models.CharField(max_length=255)
    img = models.TextField(max_length=255)
    status_text = models.CharField(max_length=255)

    def __str__(self):
        return self.status_text
