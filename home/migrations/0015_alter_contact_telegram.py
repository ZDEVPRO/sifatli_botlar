# Generated by Django 4.0.6 on 2022-07-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_subject_contact_telegram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telegram',
            field=models.CharField(max_length=600, verbose_name='Telegram'),
        ),
    ]