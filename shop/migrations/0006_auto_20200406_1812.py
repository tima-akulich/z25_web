# Generated by Django 3.0.4 on 2020-04-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200403_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image_base64',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
