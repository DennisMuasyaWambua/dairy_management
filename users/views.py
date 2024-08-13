import datetime
import jwt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from farmers_milk.models import Cow
from farmers_milk.serializers import CowSerializer
from .models import User
from .serializer import UserSerializer, LoginSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    q_set = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                phone = serializer.validated_data['phone']
                password = serializer.validated_data['password']

                user = authenticate(phone=phone, password=password)

                if user is not None:
                    refresh = RefreshToken.for_user(user)

                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'detail': "Authentication Failed",
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except AssertionError:
            return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # phone = request.data['phone']
        # password = request.data['password']
        #
        # user = User.objects.filter(phone=phone).first()
        #
        # if user is None:
        #     raise AuthenticationFailed('User not found!')
        #
        # if not user.check_password(password):
        #     raise AuthenticationFailed("Incorrect password")
        #
        # payload = {
        #     'id': user.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     'iat': datetime.datetime.utcnow()
        # }
        #
        # token = jwt.encode(payload, 'secret', algorithm='HS256')
        #
        # response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True)
        # response.data = {
        #     "token": token,
        # }
        #
        # return response


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

#
# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')
#
#         try:
#             payload = jwt.decode(token, 'secret', algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed("Unauthenticated!")
#
#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#
#         return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "Successfully logged out!"
        }
        return response


# class RegisterDairyView(APIView):
#     def post(self, request):
#         serializer = DairySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class RegisterFarmerView(APIView):
#     def post(self, request):
#         serializer = FarmerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
