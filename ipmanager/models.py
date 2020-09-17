from django.db import models
from netfields import CidrAddressField


class CidrBlock(models.Model):

    cidr_block = CidrAddressField()
    netmask = models.GenericIPAddressField(
        protocol='IPv4', blank=True, null=True, default=None)


class IpAddress(models.Model):

    cidr_block_id = models.ForeignKey(
        CidrBlock, related_name='ips', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol='IPv4')
    STATUS_CHOICES = (
        ('AC', 'Acquired'),
        ('AV', 'Available'),
    )
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default='AV')

    class Meta:
        #unique_together = ['ip_address', 'cidr_block']
        ordering = ['cidr_block_id', 'ip_address']

    def __str__(self):
        return '%s: %s' % (self.ip_address, self.status)

    @property
    def cidr_info(self):
        return '%s %s' % (self.cidr_block_id.cidr_block, self.cidr_block_id.netmask)
