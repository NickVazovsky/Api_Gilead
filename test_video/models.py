from django.db import models
import os
from account.models import Roles


def video_upload_to(instance, filename):
    return os.path.join('video', instance.name + os.path.splitext(filename)[1])

class TypeMedia(models.Model):
    name_of_type = models.CharField("Тип", max_length=100)


    def __str__(self):
        return self.name_of_type



# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    picture = models.FileField(upload_to=video_upload_to, verbose_name='Видео')
    type_media = models.ForeignKey(TypeMedia, on_delete=models.DO_NOTHING)
    roles = models.ManyToManyField(Roles, verbose_name="Контент для")


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return