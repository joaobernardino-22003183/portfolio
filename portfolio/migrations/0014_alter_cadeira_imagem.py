# Generated by Django 4.0.5 on 2022-06-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_tfc_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
