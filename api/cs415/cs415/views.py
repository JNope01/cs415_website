from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Userdaylog, Usergoals, Userinfo
from cs415.serializers import UserSerializer, UserdaylogSerializer, UsergoalsSerializer, UserinfoSerializer
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication


class UserAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class UserdaylogAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        users = Userdaylog.objects.all()
        serializer = UserdaylogSerializer(users, many=True)
        return Response({'userdaylog': serializer.data})

class UsergoalsAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        users = Usergoals.objects.all()
        serializer = UsergoalsSerializer(users, many=True)
        return Response({'usergoals': serializer.data})

class UserinfoAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        users = Userinfo.objects.all()
        serializer = UserinfoSerializer(users, many=True)
        return Response({'usersinfo': serializer.data})

class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})

class GetSingleUserdaylogAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = Userdaylog.objects.get(user_id=id)
        serializer = UserdaylogSerializer(user)
        return Response({'userinfo': serializer.data})

class GetSingleUsergoalAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = Usergoals.objects.get(user_id=id)
        serializer = UsergoalsSerializer(user)
        return Response({'userinfo': serializer.data})

class GetSingleUserinfoAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = Userinfo.objects.get(user_id=id)
        serializer = UserinfoSerializer(user)
        return Response({'userinfo': serializer.data})

class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
 
        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)
 
        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)
 
        check_pass = User.objects.filter(email = email, pass_word=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, pass_word=password)
        if user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'token': jwt_token},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)
