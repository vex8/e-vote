from django.db import models

class Caketang(models.Model):
    nama = models.CharField(max_length = 200)
    ttl = models.CharField(max_length = 40)
    visi = models.TextField()
    misi = models.TextField()
    prestasi = models.TextField()

    def __str__(self):
        return str(self.id) + ": " + self.nama

class Pemilih(models.Model): 
    nim = models.CharField(max_length = 8)
    token = models.CharField(max_length= 4, default='', null=True)
    hasvoted = models.BooleanField(default=False)
    date = models.DateTimeField('date published', null=True)
    vote = models.ForeignKey(Caketang, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.nim)
# Create your models here.
