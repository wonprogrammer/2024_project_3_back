from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCustomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "image", "user")