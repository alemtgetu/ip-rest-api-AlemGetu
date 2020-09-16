from ipmanger.models import CidrBlock, IpAddress
from rest_framework import serializers


class CidrBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CidrBlock
        fields = ['id', 'cidr_block']


class IpAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = ['id', 'cidr_block', 'ip_address', 'status']
