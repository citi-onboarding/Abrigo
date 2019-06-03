# Generated by Django 2.2.1 on 2019-06-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Apoia',
        ),
        migrations.DeleteModel(
            name='Picpay',
        ),
        migrations.RemoveField(
            model_name='contas',
            name='codigo_banco',
        ),
        migrations.RemoveField(
            model_name='contas',
            name='conta_bancaria',
        ),
        migrations.RemoveField(
            model_name='contas',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='contas',
            name='nome_titular',
        ),
        migrations.RemoveField(
            model_name='contas',
            name='numero_agencia',
        ),
        migrations.AddField(
            model_name='contas',
            name='info',
            field=models.TextField(default='Sem Info'),
        ),
    ]
