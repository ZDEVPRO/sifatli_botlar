# Generated by Django 4.0.6 on 2022-07-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Home Title',
                'verbose_name_plural': 'Home Title',
            },
        ),
    ]
