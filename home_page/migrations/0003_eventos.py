# Generated by Django 2.2.1 on 2019-05-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20190519_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='evento_image/')),
                ('local', models.TextField()),
                ('dias', models.CharField(blank=True, max_length=50, null=True)),
                ('horario', models.IntegerField(blank=True, null=True)),
                ('infoEvento', models.TextField()),
                ('infoAnimais', models.TextField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
