from rest_framework import serializers
from .models import Thread


class ThreadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('title', 'content', 'reading_date')
        # read_only_fields = ('user',)

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
