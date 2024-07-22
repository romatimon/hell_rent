# Generated by Django 4.2 on 2024-07-22 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helicopter', '0003_applications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='model_starship',
        ),
        migrations.AlterField(
            model_name='applications',
            name='helicopter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='helicopter.helicopter'),
        ),
    ]
