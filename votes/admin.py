from django.contrib import admin
from .models import Caketang, Pemilih

class PemilihAdmin(admin.ModelAdmin):
    search_fields = ['nim']
    list_display = ('nim', 'token', 'hasvoted', 'vote', 'date')
    ordering = ['nim']

admin.site.register(Caketang)
admin.site.register(Pemilih, PemilihAdmin)
# Register your models here.
