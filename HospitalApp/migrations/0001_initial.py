# Generated by Django 4.1.7 on 2024-01-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='image')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=100)),
                ('Rating', models.IntegerField()),
                ('Location', models.CharField(max_length=1000)),
            ],
        ),
    ]
