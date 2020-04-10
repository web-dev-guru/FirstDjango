# Generated by Django 3.0.5 on 2020-04-10 04:01

import delicious.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField(verbose_name='creation time')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('order_num', models.CharField(default=delicious.models.increment_number, editable=False, max_length=17)),
                ('creation_time', models.DateTimeField(verbose_name='creation time')),
            ],
        ),
        migrations.CreateModel(
            name='SpicyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spice_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious.Dish')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious.OrderHeader')),
                ('spciy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious.SpicyLevel')),
            ],
        ),
    ]
