# Generated by Django 2.2.3 on 2019-07-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20190705_0443'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='project',
            constraint=models.UniqueConstraint(fields=('url',), name='unique_url'),
        ),
    ]
