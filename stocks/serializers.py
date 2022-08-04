from rest_framework import serializers
from .models import News,NewsImages
import datetime


class NewsWriteSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    datetime = serializers.IntegerField(write_only=True)
    posted_at = serializers.DateTimeField(read_only=True)
    headline = serializers.CharField()
    image = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    related = serializers.CharField()
    source = serializers.CharField()
    summary = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    url = serializers.URLField()

    def create(self, validated_data):
        validated_data['posted_at'] = datetime.datetime.fromtimestamp(validated_data.pop('datetime'))
        images = []
        images = [image for image in validated_data.pop('image').split("https://") if image]
        instance = News.objects.filter(id=validated_data.get("id"))
        if not instance.exists():
            instance =  News.objects.create(**validated_data)
            if images:
                for image in images:
                    NewsImages.objects.create(image=image,news=instance)
            return instance
        return instance.first()


class Images(serializers.Serializer):
    image = serializers.URLField()


class NewsReadSerializer(serializers.ModelSerializer):

    images = Images(many=True)

    class Meta:
        model = News
        fields = ("id", "related", "posted_at", "headline", "source", "summary", "url", "images")