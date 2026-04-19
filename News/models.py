from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    ad = models.CharField(max_length=100)

    def __str__(self):
        return self.ad
    
class Author(models.Model):
    ad = models.CharField(max_length=100)
    resim = models.FileField(upload_to='author_images')
    bilgi = models.CharField(max_length=250)
    pozisyon = models.CharField(max_length=100)

    def __str__(self):
        return self.ad
    
class News(models.Model):
    baslik = models.CharField(max_length=100)
    resim = models.FileField(upload_to='news_images')
    tarih = models.DateField()
    icerik = models.CharField(max_length=500)
    yazar = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.baslik)
        slug = base_slug
        counter = 1

        while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.baslik
