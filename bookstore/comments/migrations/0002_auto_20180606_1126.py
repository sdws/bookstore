# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(verbose_name='评分', default=1),
        ),
        migrations.AddField(
            model_name='comments',
            name='title',
            field=models.CharField(max_length=20, verbose_name='评论标题', default=''),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=1000, verbose_name='评论内容'),
        ),
    ]
