from rest_framework.serializers import ModelSerializer

from .models import Category, City, Advert


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CityModelSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class AdvertModelSerializer(ModelSerializer):
    category = CategoryModelSerializer()
    city = CityModelSerializer()

    class Meta:
        model = Advert
        fields = ("id", "title", "description", "city", "category", "views",)  # прописал для порядка, можно прописка просто '__all__'