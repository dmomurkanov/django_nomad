from rest_framework.serializers import ModelSerializer

from .models import Category, Item


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "icon")

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ("title", "price")


class ItemDetailSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ("title", "price", "is_like", "created_at")


