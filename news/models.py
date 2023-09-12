from django.db import models
import os
from ckeditor_uploader.fields import RichTextUploadingField

def news_picture_upload_to(instance, filename):
    return os.path.join('news', instance.slug + os.path.splitext(filename)[1])


class News(models.Model):
    """
        Table news

    """
    name_of_news = models.CharField("Название новости",max_length=255)
    slug = models.SlugField(unique=True)
    picture_of_news = models.FileField(upload_to=news_picture_upload_to)
    short_description = models.CharField("Краткое описание", max_length=150)
    description = RichTextUploadingField("Описание новости")
    priority = models.PositiveIntegerField(default=1, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    available_news = models.BooleanField("Доступна", default=False)

    class Meta:
        db_table = "news"
        ordering = ['-created_at']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


    def __str__(self):
        return self.name_of_news
