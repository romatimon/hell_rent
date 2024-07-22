# Generated by Django 4.2 on 2024-07-21 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helicopter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(verbose_name='Описание')),
                ('passenger_capacity', models.IntegerField(verbose_name='Вместимость пассажиров')),
                ('range', models.IntegerField(verbose_name='Дальность полета, км')),
                ('speed', models.IntegerField(verbose_name='Максимальная скорость, км/с')),
                ('rent_price', models.FloatField(verbose_name='Стоимость аренды, 1 час')),
                ('status', models.IntegerField(choices=[(1, 'Доступен'), (0, 'Недоступен')], default=1, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Вертолет',
                'verbose_name_plural': 'Вертолеты',
                'ordering': ['id'],
            },
        ),
        migrations.AddIndex(
            model_name='helicopter',
            index=models.Index(fields=['name'], name='helicopter__name_864c1c_idx'),
        ),
    ]
