# Generated by Django 3.0.4 on 2020-04-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200403_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='subcategories',
            field=models.ManyToManyField(blank=True, related_name='_category_subcategories_+', to='shop.Category', verbose_name='Subcategories'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=20, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='shop.Category', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.PositiveIntegerField(verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image_base64',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('en', 'English'), ('ru', 'Русский'), ('be', 'Belarus')], max_length=10, verbose_name='Lang')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'abstract': False,
                'unique_together': {('lang', 'item')},
            },
        ),
    ]
