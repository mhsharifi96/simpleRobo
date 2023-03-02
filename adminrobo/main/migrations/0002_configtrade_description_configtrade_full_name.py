# Generated by Django 4.1.7 on 2023-02-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configtrade',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='configtrade',
            name='full_name',
            field=models.CharField(default='', max_length=55),
            preserve_default=False,
        ),
    ]
