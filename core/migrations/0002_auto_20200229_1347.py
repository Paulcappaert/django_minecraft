# Generated by Django 3.0.3 on 2020-02-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='mc_username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
