from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer
from rest_framework import serializers
from users.models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = BaseUserCreateSerializer.Meta.model
        fields = ['id','email','password','first_name','last_name','address','phone_number']
        extra_kwargs = {
            'password': {'write_only':True}
        }

class UserSerializer(BaseUserSerializer):
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)
    class Meta(BaseUserSerializer.Meta):
        model = BaseUserSerializer.Meta.model
        ref_name = 'CustomUser'
        fields = ['id','email','role','first_name','last_name','address','phone_number']


