# Generated by Django 3.1.6 on 2021-02-12 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kotki', '0002_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
