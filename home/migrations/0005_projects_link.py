# Generated by Django 4.0.6 on 2022-07-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.CharField(default='link', max_length=1000),
            preserve_default=False,
        ),
    ]
