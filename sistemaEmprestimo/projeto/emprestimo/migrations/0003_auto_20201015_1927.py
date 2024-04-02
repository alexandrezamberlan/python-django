# Generated by Django 3.1.2 on 2020-10-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_auto_20201015_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='devolvido',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='em_emprestimo',
            field=models.BooleanField(default=False, verbose_name='Selecione se o objeto estiver emprestado '),
        ),
    ]
