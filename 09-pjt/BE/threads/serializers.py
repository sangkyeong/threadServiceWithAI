from rest_framework import serializers
from .models import Thread, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'thread')

class ThreadListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Thread
        fields = '__all__'

    def get_like_count(self, obj):
        return obj.likes.count()

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('title', 'content', 'reading_date')
        read_only_fields = ('user',)

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
