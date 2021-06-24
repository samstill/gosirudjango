# Generated by Django 3.2.4 on 2021-06-24 04:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]