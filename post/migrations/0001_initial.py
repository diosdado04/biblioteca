# Generated by Django 5.0.6 on 2024-05-14 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('editorial', models.TextField()),
                ('best_seller', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('author', models.ManyToManyField(to='post.author')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sold', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.book')),
            ],
        ),
    ]
