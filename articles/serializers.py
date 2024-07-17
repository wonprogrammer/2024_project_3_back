from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Article
        fields = ("pk", "title", "content", "image", "updated_at", "user")


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "content", "image")
