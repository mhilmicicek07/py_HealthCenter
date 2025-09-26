from django.db import models
from django.utils.text import slugify

# Create your models here.
class Team(models.Model):
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to='team_images')
    brans = models.CharField(max_length=50)
    dahili = models.CharField(max_length=15)
    email = models.EmailField()
    ozgecmis = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isim