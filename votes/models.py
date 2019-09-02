from django.db import models

class Token(models.Model):
    token = models.CharField(max_length = 4)
    used = models.BooleanField(default=False)

class Pemilih(models.Model): 
    nim = models.CharField(max_length = 8)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    vote = models.IntegerField(default = 0)


class Caketang(models.Model):
    nama = models.CharField(max_length = 200)
    ttl = models.CharField(max_length = 20)
    visi = models.TextField()
    misi = models.TextField()
    prestasi = models.TextField()

    def __str__(self):
        return str(self.id) + ": "+self.nama

# Create your models here.
