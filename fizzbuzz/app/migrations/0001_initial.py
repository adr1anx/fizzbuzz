# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FizzBuzz',
            fields=[
                ('fizzbuzz_id', models.AutoField(serialize=False, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('useragent', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
