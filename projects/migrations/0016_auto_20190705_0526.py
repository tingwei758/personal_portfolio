# Generated by Django 2.2.3 on 2019-07-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20190705_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='filename',
            field=models.CharField(default='project_detail.html', max_length=100),
        ),
        migrations.DeleteModel(
            name='ProjectHTML',
        ),
    ]