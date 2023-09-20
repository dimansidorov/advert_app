from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from .models import Advert
from .serializers import AdvertModelSerializer


class AdvertListAPIView(ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertModelSerializer


class AdvertRetrieveAPIView(RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertModelSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
