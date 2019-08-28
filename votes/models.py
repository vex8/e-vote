from django.db import models

class Pemilih(models.Model): 
    nim = models.CharField(max_length = 8)
    token = models.CharField(max_length = 4)
    date = models.DateTimeField('date published')
    vote = models.IntegerField(default = 0)


class Caketang(models.Model):
    nama = models.CharField(max_length = 200)
    ttl = models.CharField(max_length = 20)
    visi = models.CharField(max_length = 2000)
    misi = models.CharField(max_length = 2000)
    prestasi = models.CharField(max_length = 2000)

    def __str__(self):
        return str(self.id)
# Create your models here.
