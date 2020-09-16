from django.shortcuts import render
from rest_framework import viewsets, status
from ipmanager.models import CidrBlock, IpAddress
from ipmanager.serializers import CidrBlockSerializer, IpAddressSerializer
from ipaddress import IPv4Address, IPv4Network
from rest_framework.response import Response


class CidrBlockViewSet(viewsets.ModelViewSet):

    queryset = CidrBlock.objects.all()
    serializer_class = CidrBlockSerializer

    # when CidrBlock is created create
    # all the IP address in that block
    def create(self, request):
        cidr = request.POST['cidr_block']

        if cidr:
            try:
                cidr_net_obj = IPv4Network(cidr, strict=False)
            except Exception:
                return Response(cidr_net_obj.errors, status=status.HTTP_400_BAD_REQUEST)

            cidr_model_obj = CidrBlock.objects.create(cidr_block=cidr)
            # cidr_model_obj.save()
            for ip in list(cidr_net_obj.hosts()):
                ip_add = IpAddress.objects.get_or_create(ip_address=str(
                    ip), cidr_block=cidr_model_obj)
            return Response('Succesfully created CIDR and all IPs in the block', status=status.HTTP_201_CREATED)
        return Response('Invalid CIDR input', status=status.HTTP_400_BAD_REQUEST)


class IpAddressViewSet(viewsets.ModelViewSet):

    queryset = IpAddress.objects.all()
    serializer_class = IpAddressSerializer

    def create(self, request):
        return Response('Create CIDR block to create the IP if not in the list', status=status.HTTP_400_BAD_REQUEST)
