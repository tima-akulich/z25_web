# Generated by Django 3.0.4 on 2020-04-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200403_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requesterror',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_base64',
            field=models.TextField(default=None, null=True),
        ),
    ]
