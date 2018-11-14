from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.files.storage import FileSystemStorage
from django.conf import settings

upload_storage = FileSystemStorage(location=settings.MEDIA_ROOT)


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    featured_image = models.ImageField(default="", blank=True, upload_to='image')
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title