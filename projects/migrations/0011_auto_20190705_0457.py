# Generated by Django 2.2.3 on 2019-07-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20190705_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
    ]
