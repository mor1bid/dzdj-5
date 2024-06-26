# Generated by Django 5.0.3 on 2024-03-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzproj', '0002_rename_orders_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('uid', models.IntegerField(default=0, unique=True)),
                ('wid', models.IntegerField(default=0, unique=True)),
                ('bill', models.DecimalField(decimal_places=2, max_digits=8)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
