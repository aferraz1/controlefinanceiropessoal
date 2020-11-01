# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-15 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=40, verbose_name='Descrição')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Saldo')),
            ],
            options={
                'ordering': ['-saldo', 'descricao'],
            },
        ),
    ]
