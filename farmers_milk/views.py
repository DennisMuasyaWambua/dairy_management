from rest_framework.generics import ListAPIView

from .serializers import CowSerializer, MilkSerializer
from .models import Cow, Milk
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


# create cow / see cows for different farmers

class CreateCowView(APIView):
    serializer_class = CowSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        current_user = request.user

        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': 'Invalid data provided!',
                'error': serializer.errors
            }, status=HTTP_400_BAD_REQUEST)

        #        Getting the data
        cow_name = request.data.get('cow_name')
        breed = request.data.get('breed')

        if not User.exists():
            return Response({
                'status': False,
                'message': 'Such a user does not exist',
                'error': serializer.errors
            }, status=HTTP_404_NOT_FOUND)
        farmer = User.first()

        cow = Cow(farmer=farmer, cow_name=cow_name, breed=breed)

        if current_user.is_authenticated():
            cow.save()
            return Response({
                'status': True,
                'message': 'Cow saved successfully!'
            }, status=HTTP_201_CREATED)
        else:
            return Response({
                'status': False,
                'message': 'Cow not recorded'
            }, status=HTTP_409_CONFLICT)


# record milk  view/ see milk records of a cow

class GetCowsView(ListAPIView):
    queryset = Cow.objects.all()
    serializer_class = CowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.cow_set.all()
