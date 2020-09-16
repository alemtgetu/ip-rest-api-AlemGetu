from django.shortcuts import render
from rest_framework import viewsets
from ipmanager.models import CidrBlock, IpAddress
from ipmanager.serializers import CidrBlockSerializer, IpAddressSerializer


class CidrBlockViewSet(viewsets.ModelViewSet):

    queryset = CidrBlock.objects.all()
    serializer_class = CidrBlockSerializer


class IpAddressViewSet(viewsets.ModelViewSet):

    queryset = IpAddress.objects.all()
    serializer_class = IpAddressSerializer
