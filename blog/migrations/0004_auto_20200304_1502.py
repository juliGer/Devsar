# Generated by Django 3.0.3 on 2020-03-04 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200304_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='cancha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='canchas', to='blog.Cancha'),
        ),
    ]