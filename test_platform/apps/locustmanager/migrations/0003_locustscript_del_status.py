# Generated by Django 2.2.1 on 2019-06-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locustmanager', '0002_auto_20190611_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='locustscript',
            name='del_status',
            field=models.IntegerField(default=0, verbose_name='是否删除'),
        ),
    ]
