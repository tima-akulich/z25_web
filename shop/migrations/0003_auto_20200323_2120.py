# Generated by Django 3.0.4 on 2020-03-23 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_myfirstmodel_number_column'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('1', 'Category_name_1'), ('2', 'Category_name_2'), ('3', 'Category_name_3'), ('4', 'Category_name_4')], max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Company', to_field='name')),
            ],
        ),
        migrations.DeleteModel(
            name='MyFirstModel',
        ),
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(through='shop.Order', to='shop.Product'),
        ),
    ]
