# Generated by Django 4.0.6 on 2022-08-22 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0010_rename_author_noticia_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=models.TextField(default=django.utils.timezone.now),
        ),
    ]
