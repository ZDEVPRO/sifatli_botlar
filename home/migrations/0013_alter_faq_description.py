# Generated by Django 4.0.6 on 2022-07-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_contact_create_date_alter_contact_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Javob'),
        ),
    ]
