import datetime
from rest_framework.viewsets import ReadOnlyModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .models import News
from rest_framework.views import APIView
from .serializers import NewsReadSerializer, NewsWriteSerializer
from rest_framework import filters
from rest_framework.response import Response
from .tasks import get_news_by_stock
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class NewsView(ReadOnlyModelViewSet):

    serializer_class = NewsReadSerializer
    queryset = News.objects.all()
    lookup_field = "related"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_fields = {}
        if self.request.query_params.get("date_from"):
            filter_fields['posted_at__gte'] = self.request.query_params.get('date_from')
        if self.request.query_params.get("date_to"):
            filter_fields['posted_at__lte'] = self.request.query_params.get("date_to")
        if filter_fields:
            return queryset.filter(**filter_fields)
        return queryset.filter()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        data = queryset.filter(**filter_kwargs)
        return data


    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data,many=True)
        return Response(serializer.data)