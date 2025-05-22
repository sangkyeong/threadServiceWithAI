from rest_framework import serializers
from .models import Book


# # articles/serializers.py
# class ArticleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'content')


# # articles/serializers.py
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'
#         read_only_fields = ('user',)
