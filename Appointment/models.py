from django.db import models

# Create your models here.

class Bolum(models.Model):
    ad = models.CharField(max_length=100)

    def __str__(self):
        return self.ad
    
class Randevu(models.Model):
    isim = models.CharField(max_length=200)
    email = models.EmailField()
    telefon = models.CharField(max_length=15)
    tarih = models.DateField()
    saat = models.TimeField()
    bolum = models.ForeignKey(Bolum, on_delete=models.CASCADE)
    mesaj = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.isim} - {self.tarih} {self.saat}"