# Generated by Django 2.2.1 on 2019-06-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20190603_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='info',
            field=models.TextField(default='Conta: <br> Banco: '),
        ),
    ]
