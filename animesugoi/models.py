from django.db import models
from django.utils.text import slugify

STATUS = (
    ("aired","aired"),
    ("notaired","notaired")
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=220, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Anime(models.Model):
    anime_name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    episodes = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to="anime_cover_image")
    documents = models.FileField(upload_to="anime_documents")
    status = models.CharField(max_length=300, choices=STATUS)
    description = models.TextField()
