# Generated by Django 2.2.4 on 2019-09-12 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_auto_20190911_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemilih',
            name='token',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.Token'),
        ),
        migrations.AlterField(
            model_name='pemilih',
            name='vote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.Caketang'),
        ),
    ]
