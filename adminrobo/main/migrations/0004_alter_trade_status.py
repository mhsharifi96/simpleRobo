# Generated by Django 4.1.7 on 2023-03-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_price_trade_last_trade_price_trade_first_asks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('close', 'close'), ('not_active', 'not_active')], max_length=15),
        ),
    ]
