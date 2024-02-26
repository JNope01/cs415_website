from rest_framework import serializers
from cs415.models import User, Userdaylog, Usergoals, Userinfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserdaylogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdaylog
        fields = '__all__'

class UsergoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usergoals
        fields = '__all__'

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'