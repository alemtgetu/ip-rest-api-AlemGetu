# Generated by Django 3.1.1 on 2020-09-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipmanager', '0002_auto_20200916_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='status',
            field=models.CharField(choices=[('AC', 'Acquired'), ('AV', 'Available')], default='AV', max_length=2),
        ),
    ]
