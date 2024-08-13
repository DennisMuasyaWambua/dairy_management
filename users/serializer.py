from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        # instance.save()
        # return instance


# class DairySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dairy
#         fields = ["name", "id_number", "phone", "location", "password"]
#
#
# class FarmerSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     dairy = DairySerializer()
#
#     class Meta:
#         model = Farmer
#         fields = ["name", "id_number", "phone", "location", "password"]
#
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)