from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from account.api.serializer import AccountPropertySerializer

from account.models import Account
from account.api.serializer import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST',])
def registration_view(request):

    if request.method =="POST":
        serializer=RegistrationSerializer(data=request.data)
        data={

        }
        if serializer.is_valid():
            account=serializer.save()
            data['response']='Successfully Register New User'
            data['email']=account.email
            data['username']=account.username
            token=Token.objects.get(user=account).key
            data['token']=token


        else:
            data=serializer.errors
        return Response(data)

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def account_property_view(request):
    try:
        account=request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer=AccountPropertySerializer(account)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def update_account_property_view(request):
    try:
        account=request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='PUT':
        serializer=AccountPropertySerializer(account,data=request.data)
        data={

        }
        if serializer.is_valid():
            serializer.save()
            data['response']='Account Updated Successfully'
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
