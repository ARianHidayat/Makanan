# Generated by Django 4.2.7 on 2023-11-30 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hidayat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailtransaksi',
            options={'verbose_name_plural': 'Detail Transaksi'},
        ),
        migrations.AlterModelOptions(
            name='transaksi',
            options={'verbose_name_plural': 'Transaksi'},
        ),
    ]
