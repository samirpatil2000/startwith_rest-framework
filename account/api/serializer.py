from rest_framework import serializers
from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model=Account
        fields = ['email', 'username', 'password', 'password2']

    def save(self, **kwargs):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        #TODO validated_data is ==== is_valid ()

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account

class AccountPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['pk','username','email']

