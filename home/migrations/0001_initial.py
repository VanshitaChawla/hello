# Generated by Django 4.1 on 2022-09-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=254)),
                ('phoneno', models.CharField(max_length=10)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
