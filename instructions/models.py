from django.db import models


# Create your models here.
class Instructions(models.Model):
    title = models.CharField("Название", max_length=255)
    preview = models.FileField("Превью", upload_to='instruction/preview')
    pdf = models.FileField("Пдф", upload_to='instruction/pdf')
    available = models.BooleanField(default=True)
    position_number = models.PositiveIntegerField(default=1, verbose_name="Позиционный номер")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'
        ordering = ['position_number']