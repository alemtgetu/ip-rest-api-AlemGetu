from rest_framework import serializers
from ipmanager.models import CidrBlock, IpAddress


class CidrBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CidrBlock
        fields = ['id', 'cidr_block']


class IpAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = ['id', 'cidr_block', 'ip_address', 'status']
