from django.core.management.base import BaseCommand
import os
import csv
from votes.models import Caketang, Pemilih

class Command(BaseCommand):
  help = 'Populate database with file'
  def add_arguments(self, parser):
    parser.add_argument('file', type=str, help='The file to be used')
    parser.add_argument('table', type=str, help='Table to populate')

  def handle(self, *args, **kwargs):
    file = kwargs['file'] or 'dba.csv'
    with open(kwargs['file']) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        if kwargs['table'].lower() == 'pemilih':
          _,created = Pemilih.objects.get_or_create(
            nim=row['NIM'],
            token=None,
            date=None,
            vote=None
          )
          print(row['NIM'], created)
        elif kwargs['table'].lower() == 'caketang':
          _,created = Caketang.objects.get_or_create(
            nama=row['Nama'],
            ttl=row['TTL'],
            visi=row['Visi'],
            misi=row['Misi'],
            prestasi=row['Prestasi']
          )
          print(row['Nama'], created)
    print('finished populating')