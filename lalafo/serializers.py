from rest_framework import serializers
from .models import *


class UserSeriaziler(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'phoneNumber', 'picture']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'product', 'user_id', 'price', 'currency', 'picture', 'description', 'category', 'location', 'user'
        ]

    def to_representation(self, instance):
        self.fields['user'] = UserSeriaziler(read_only=True)
        return super(ProductSerializer, self).to_representation(instance)
