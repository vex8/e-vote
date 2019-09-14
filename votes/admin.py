from django.contrib import admin
from .models import Caketang, Pemilih

class PemilihAdmin(admin.ModelAdmin):
    list_display = ('nim', 'token', 'hasvoted', 'vote', 'date')

admin.site.register(Caketang)
admin.site.register(Pemilih)
# Register your models here.
