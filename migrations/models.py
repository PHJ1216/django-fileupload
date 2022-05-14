from django.db import models


# Create your models here.

class FileUpload(models.Model):
    title = models.TextField(max_length=40, null=True, blank=True)
    imgfile = models.ImageField(null=True, upload_to="media/%Y/%m/%d", blank=False)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
