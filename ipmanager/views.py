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
            # make sure the CIDR entry is valid CIDR entry
            # by creating IPv4Network Object with it
            try:
                cidr_net_obj = IPv4Network(cidr, strict=True)
            except Exception:
                return Response('Invalid CIDR entry.', status=status.HTTP_400_BAD_REQUEST)

            # create CIDR model object with the cidr input from request and
            # with the netmask from CIDR IPv4Network object
            # cidr_model_obj = CidrBlock.objects.create(cidr_block=cidr, netmask=str(cidr_net_obj.netmask))'''

            ''' using get object by CIDR gives 
                sqlite InterfaceError: Error binding parameter 0 - probably unsupported type
            
            try:
                cidr_model_obj = CidrBlock.objects.get(cidr_block=cidr)
                #cidr_model_obj.netmask = str(cidr_net_obj.netmask)
                return Response('CIDR already EXIST', status=status.HTTP_201_CREATED)
            except CidrBlock.DoesNotExist:
                cidr_model_obj = CidrBlock(
                    cidr_block=cidr, netmask=str(cidr_net_obj.netmask))
                cidr_model_obj.save()'''
            # work around
            cidr_model_obj = CidrBlock.objects.raw(
                'SELECT * FROM ipmanager_cidrblock where cidr_block='+'"'+cidr+'"')
            if (cidr_model_obj.__len__() > 0):
                return Response('CIDR already EXIST', status=status.HTTP_208_ALREADY_REPORTED)
            else:
                cidr_model_obj = CidrBlock(
                    cidr_block=cidr, netmask=str(cidr_net_obj.netmask))
                cidr_model_obj.save()
            ##################

            # create all IPs in the CIDR block
            # the IPs will be stored in IPAddress Table
            for ip in list(cidr_net_obj.hosts()):
                '''try:
                    ip_add = IpAddress.objects.get(ip_address=str(ip))
                    ip_add.cidr_block = cidr_model_obj
                except IpAddress.DoesNotExist:
                    ip_add = IpAddress(ip_address=str(
                        ip), cidr_block=cidr_model_obj)
                ip_add.save()'''
                ip_add = IpAddress.objects.get_or_create(ip_address=str(
                    ip), cidr_block_id=cidr_model_obj)
            return Response('Succesfully created CIDR and all IPs in the block', status=status.HTTP_201_CREATED)
        return Response('Invalid CIDR input', status=status.HTTP_400_BAD_REQUEST)


class IpAddressViewSet(viewsets.ModelViewSet):

    queryset = IpAddress.objects.all()
    serializer_class = IpAddressSerializer

    def create(self, request):
        return Response('Create CIDR block to create the IP if not in the list', status=status.HTTP_400_BAD_REQUEST)
