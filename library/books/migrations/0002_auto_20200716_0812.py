# Generated by Django 3.0.8 on 2020-07-16 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('id',)},
        ),
    ]
