# Generated by Django 4.1.4 on 2023-02-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0003_rename_relase_year_movie_release_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pic_url',
            field=models.URLField(blank=True, db_column='pic_url', max_length=512, null=True),
        ),
    ]