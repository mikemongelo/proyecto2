# Generated by Django 4.0.6 on 2022-08-15 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0006_alter_noticia_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('historia', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
    ]