from django.db import models
from account.models import Roles
from .managers import MaterialManager
from .upload_path import preview_upload_to, material_upload_to, poster_upload_to
from ckeditor_uploader.fields import RichTextUploadingField


class SelectionMaterial(models.Model):
    """
    Разделы материалов
    """
    name_of_selection = models.CharField("Название", max_length=255)
    slug = models.SlugField(unique=True, verbose_name="ЧПУ")

    class Meta:
        db_table = 'selection_material'
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name_of_selection


class PatientProfiles(models.Model):
    """
    Профиль пациента
    """
    name_of_profile = models.CharField("Название", max_length=255)

    class Meta:
        db_table = 'patient_profile'
        verbose_name = 'Профиль пациента'
        verbose_name_plural = 'Профили пациентов'

    def __str__(self):
        return self.name_of_profile


class ContentFormat(models.Model):
    """
    Таблица для выбора формата
    """
    type_name = models.CharField("Тип контента", max_length=255)

    class Meta:
        db_table = 'content_format'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.type_name


class ProductMaterial(models.Model):
    """
    Таблица Продуктов
    """
    product_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_material'
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.product_name


class Tags(models.Model):
    name_tags = models.CharField(max_length=255)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name_tags


class Material(models.Model):
    """
    Таблица материалов
    """
    name_material = models.CharField("Название материала", max_length=255)
    slug = models.SlugField("ЧПУ", unique=True)
    content_format = models.ForeignKey(ContentFormat, on_delete=models.CASCADE, verbose_name='Тип контента')
    selection = models.ForeignKey(SelectionMaterial, on_delete=models.CASCADE, verbose_name="Раздел", blank=True, null=True)
    publication = RichTextUploadingField("Публикация", blank=True, null=True)
    roles = models.ManyToManyField(Roles, verbose_name='Для кого контент')
    product_material = models.ForeignKey(ProductMaterial, on_delete=models.CASCADE, verbose_name="Продукт")
    patient_profile = models.ManyToManyField(PatientProfiles, verbose_name='Профиль пациента')
    material_files = models.FileField("Материал", upload_to=material_upload_to, blank=True, null=True)
    tags = models.ManyToManyField(Tags, verbose_name='Тег')
    poster = models.ImageField("Постер", upload_to=poster_upload_to, blank=True, null=True)
    preview = models.ImageField("Превью", upload_to=preview_upload_to, blank=True, null=True)
    expiration_date = models.DateField("Дата истечения контента", blank=True, null=True)
    priority = models.PositiveIntegerField("Приоритетность", default=1)
    created_at = models.DateField("Дата добавления", auto_now_add=True)
    updated_at = models.DateField("Дата обновления", auto_now=True)

    objects = MaterialManager()

    class Meta:
        db_table = 'material'
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.name_material
