# Generated by Django 3.1.1 on 2020-09-16 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CidrBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidr_block', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('status', models.CharField(default='Available', max_length=20)),
                ('cidr_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ips', to='ipmanager.cidrblock')),
            ],
        ),
    ]
