# Generated by Django 3.1.1 on 2020-09-16 18:59

from django.db import migrations
import netfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ipmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidrblock',
            name='cidr_block',
            field=netfields.fields.CidrAddressField(max_length=43),
        ),
    ]