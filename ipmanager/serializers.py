from rest_framework import serializers
from ipmanager.models import CidrBlock, IpAddress


class CidrBlockSerializer(serializers.ModelSerializer):

    '''can show all ips of the cidr block with statu
    IpAdress Model for more __str__ method includes the ip address and its status
    not good idea to show all IP when listing CIDR, because there could be thousands of IP per CIDR
    '''
    # ips = serializers.StringRelatedField(many=True)

    class Meta:
        model = CidrBlock
        fields = ['id', 'cidr_block', 'netmask']  # , 'ips']


class IpAddressSerializer(serializers.ModelSerializer):

    # cidr_block = serializers.SlugRelatedField(
    #   read_only=True, slug_field='cidr_block')
    cidr_info = serializers.ReadOnlyField()

    class Meta:
        model = IpAddress
        fields = ['id', 'cidr_block_id', 'cidr_info', 'ip_address', 'status']
