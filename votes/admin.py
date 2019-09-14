from django.contrib import admin
from .models import Caketang, Pemilih

class CaketangAdmin(admin.ModelAdmin):
    pass

class PemilihAdmin(admin.ModelAdmin):
    pass

admin.site.register(Caketang)
admin.site.register(Pemilih)
# Register your models here.
