from rest_framework import serializers
from .models import Thread, Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_writers_name = serializers.SerializerMethodField()
    content = serializers.CharField(
        error_messages={
            'blank': '댓글을 입력해주세요.',
            'required': '댓글은 필수 항목입니다.',
        }
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'thread')

    def get_comment_writers_name(self, obj):
        return obj.user.username if obj.user else None
    
    def validate(self, data):
        errors = {}
        
        content = data.get('content')
        if not content or not content.strip():
            errors['content'] = ['댓글을 입력해주세요.']

        if errors:
            raise serializers.ValidationError(errors)

        return data

class ThreadListSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    writers_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Thread
        fields = '__all__'

    def get_comments(self, obj):
        comments_qs = obj.comments.order_by('-created_at')
        return CommentSerializer(comments_qs, many=True).data

    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_liked(self, obj):
        user = self.context.get('user')
        if user:
            return user in obj.likes.all()
        return False
    
    def get_writers_name(self, obj):
        return obj.user.username

class ThreadSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        error_messages={
            'blank': '제목을 입력해주세요.',
            'required': '제목은 필수 항목입니다.',
        }
    )

    content = serializers.CharField(
        error_messages={
            'blank': '내용을 입력해주세요.',
            'required': '내용은 필수 항목입니다.',
        }
    )

    reading_date = serializers.CharField(
        error_messages={
            'blank': '읽은 날짜를 입력해주세요.',
            'required': '읽은 날짜는 필수 항목입니다.',
        }
    )

    class Meta:
        model = Thread
        fields = ('title', 'content', 'reading_date')
        read_only_fields = ('user',)    

    def validate(self, data):
        errors = {}
        
        title = data.get('title')
        if not title or not title.strip():
            errors['title'] = ['제목을 입력해주세요.']

        content = data.get('content')
        if not content or not content.strip():
            errors['content'] = ['내용을 입력해주세요.']

        reading_date = data.get('reading_date')
        if not reading_date or not reading_date.strip():
            errors['reading_date'] = ['읽은 날짜를 입력해주세요.']

        if errors:
            raise serializers.ValidationError(errors)

        return data