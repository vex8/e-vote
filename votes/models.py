from django.db import models

class Token(models.Model):
    token = models.CharField(max_length = 4)
    used = models.BooleanField(default=False)
    def __str__(self):
        return str(self.token)

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
    token = models.OneToOneField(Token, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField('date published', null=True)
    vote = models.ForeignKey(Caketang, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.nim)
# Create your models here.
