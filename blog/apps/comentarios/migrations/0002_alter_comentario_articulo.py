# Generated by Django 5.1.2 on 2024-10-19 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='articulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.articulo'),
        ),
    ]