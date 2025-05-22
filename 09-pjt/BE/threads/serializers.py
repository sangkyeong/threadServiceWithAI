from rest_framework import serializers
from .models import Thread


# articles/serializers.py
# class ArticleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Thread
#         fields = ('id', 'title', 'content')


# # articles/serializers.py
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Thread
#         fields = '__all__'
#         read_only_fields = ('user',)
