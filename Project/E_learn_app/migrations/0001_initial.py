# Generated by Django 3.2.4 on 2021-10-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.URLField(max_length=300)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=300)),
                ('image', models.ImageField(upload_to='static')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
    ]
