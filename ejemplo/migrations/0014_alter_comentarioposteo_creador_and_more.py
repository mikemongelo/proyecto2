# Generated by Django 4.0.6 on 2022-08-25 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ejemplo', '0013_comentarioposteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarioposteo',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentarioposteo',
            name='posteo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ejemplo.noticia'),
        ),
    ]
