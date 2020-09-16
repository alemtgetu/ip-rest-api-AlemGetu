from django.db import models
from netfields import CidrAddressField


class CidrBlock(models.Model):

    cidr_block = CidrAddressField()


class IpAddress(models.Model):

    cidr_block = models.ForeignKey(
        CidrBlock, related_name='ips', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol='IPv4')
    status = models.CharField(max_length=20, default='Available')
