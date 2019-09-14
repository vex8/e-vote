from django.contrib import admin
from .models import Caketang, Pemilih

class PemilihAdmin(admin.ModelAdmin):
    list_display = ('nim', 'token', 'hasvoted', 'vote', 'date')
    search_fields = ['nim']

admin.site.register(Caketang)
admin.site.register(Pemilih, PemilihAdmin)
# Register your models here.
