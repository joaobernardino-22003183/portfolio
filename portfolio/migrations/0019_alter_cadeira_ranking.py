# Generated by Django 4.0.5 on 2022-06-12 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_cadeira_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ranking',
            field=models.CharField(max_length=40),
        ),
    ]
