# serializers.py
from rest_framework import serializers
from .models import User
from books.models import Category


class PureRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        error_messages={
            'blank': '비밀번호를 입력해주세요.',
            'required': '비밀번호는 필수 항목입니다.',
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        error_messages={
            'blank': '비밀번호 확인을 입력해주세요.',
            'required': '비밀번호 확인은 필수 항목입니다.',
        }
    )

    username = serializers.CharField(
        required=True,
        error_messages={
            'blank': '아이디를 입력해주세요.',
            'required': '아이디는 필수 항목입니다.',
        }
    )
    email = serializers.EmailField(
        required=True,
        error_messages={
            'blank': '이메일을 입력해주세요.',
            'required': '이메일은 필수 항목입니다.',
        }
    )

    gender = serializers.ChoiceField(
        choices=User.GENDER_CHOICES,
        required=True,
        allow_blank=False,
        error_messages={
            'required': '성별을 선택해주세요.',
            'null': '성별을 선택해주세요.',
            'invalid_choice': '유효한 성별을 선택해주세요.'
        }
    )
    age = serializers.IntegerField(
        required=True,
        allow_null=False,
        error_messages={
            'required': '나이를 입력해주세요.',
            'invalid': '나이는 숫자여야 합니다.',
            'null': '나이를 입력해주세요.'
        }
    )

    profile_img = serializers.ImageField(required=False)
    weekly_avg_reading_time = serializers.IntegerField(required=False)
    interested_genres = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
            'gender', 'age', 'profile_img', 'weekly_avg_reading_time', 'interested_genres'
        ]

    def validate(self, data):
        errors = {}

        # username: 빈 값, 중복 체크
        username = data.get('username')
        if not username or not username.strip():
            errors['username'] = ['아이디를 입력해주세요.']
        elif User.objects.filter(username=username).exists():
            errors['username'] = ['이미 사용 중인 아이디입니다.']

        # email: 빈 값 체크
        email = data.get('email')
        if not email or not email.strip():
            errors['email'] = ['이메일을 입력해주세요.']
        elif User.objects.filter(email=email).exists():
            errors['email'] = ['이미 사용 중인 이메일입니다.']

        # password1: 빈 값, 길이 체크
        password1 = data.get('password1')
        if not password1 or not password1.strip():
            errors['password1'] = ['비밀번호를 입력해주세요.']
        elif len(password1) < 8:
            errors['password1'] = ['비밀번호는 8자 이상이어야 합니다.']

        # password2: 빈 값 체크
        password2 = data.get('password2')
        if not password2 or not password2.strip():
            errors['password2'] = ['비밀번호 확인을 입력해주세요.']

        # password1, password2 일치 체크 (둘 다 입력된 경우만)
        if password1 and password2 and password1 != password2:
            errors['password2'] = ['비밀번호가 일치하지 않습니다.']

        # gender: 빈 값 체크
        gender = data.get('gender')
        if not gender:
            errors['gender'] = ['성별을 선택해주세요.']

        # age: 빈 값 체크
        age = data.get('age')
        if age is None:
            errors['age'] = ['나이를 입력해주세요.']

        # 추가 검증 필요시 여기에...

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')

        interested_genres = validated_data.pop('interested_genres', [])
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        if interested_genres:
            user.interested_genres.set(interested_genres)

        return user


class PureUpdateSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        error_messages={
            'blank': '이메일을 입력해주세요.',
            'required': '이메일은 필수 항목입니다.',
        }
    )

    gender = serializers.ChoiceField(
        choices=User.GENDER_CHOICES,
        required=True,
        allow_blank=False,
        error_messages={
            'required': '성별을 선택해주세요.',
            'null': '성별을 선택해주세요.',
            'invalid_choice': '유효한 성별을 선택해주세요.'
        }
    )
    age = serializers.IntegerField(
        required=True,
        allow_null=False,
        error_messages={
            'required': '나이를 입력해주세요.',
            'invalid': '나이는 숫자여야 합니다.',
            'null': '나이를 입력해주세요.'
        }
    )

    profile_img = serializers.ImageField(required=False)
    weekly_avg_reading_time = serializers.IntegerField(required=False)
    annual_reading_amount = serializers.IntegerField(required=False)
    interested_genres = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = User
        fields = [
            'username', 'email',
            'gender', 'age', 'profile_img', 'weekly_avg_reading_time', 'annual_reading_amount', 'interested_genres'
        ]
        read_only_fields = ('username',)

    def validate(self, data):
        errors = {}

        # email: 빈 값 체크
        email = data.get('email')
        if not email or not email.strip():
            errors['email'] = ['이메일을 입력해주세요.']
        elif User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            errors['email'] = ['이미 사용 중인 이메일입니다.']

        # gender: 빈 값 체크
        gender = data.get('gender')
        if not gender:
            errors['gender'] = ['성별을 선택해주세요.']

        # age: 빈 값 체크
        age = data.get('age')
        if age is None:
            errors['age'] = ['나이를 입력해주세요.']

        # 추가 검증 필요시 여기에...

        if errors:
            raise serializers.ValidationError(errors)

        return data
    
    def update(self, instance, validated_data):
        interested_genres = validated_data.pop('interested_genres', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if interested_genres is not None:
            instance.interested_genres.set(interested_genres)
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    interested_genres_name = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)
    is_follow = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'gender',
            'age',
            'weekly_avg_reading_time',
            'annual_reading_amount',
            'profile_img',
            'interested_genres',
            'interested_genres_name',
            'followings_count',
            'followers_count',
            'gender_display',
            'is_follow',
        )

    def get_interested_genres_name(self, obj):
        return [genre.name for genre in obj.interested_genres.all()]
    
    def get_followers_count(self, obj):
        return obj.followers.count()
    
    def get_followings_count(self, obj):
        return obj.followings.count()
    
    def get_is_follow(self, obj):
        request = self.context.get('request')
        if not request:
            return False  # 로그인 안 한 경우 팔로우 안 한 것으로 처리
        return obj.followers.filter(pk=request.user.pk).exists()

class passwordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        error_messages={
            'blank': '현재 비밀번호를 입력해주세요.',
            'required': '현재 비밀번호는 필수 항목입니다.',
        }
    )
    password1 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        error_messages={
            'blank': '새 비밀번호를 입력해주세요.',
            'required': '새 비밀번호는 필수 항목입니다.',
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        error_messages={
            'blank': '새 비밀번호 확인을 입력해주세요.',
            'required': '새 비밀번호 확인은 필수 항목입니다.',
        }
    )

    class Meta:
        model = User
        fields = [
            'current_password', 'password1', 'password2',
        ]

    def validate(self, data):
        errors = {}

        user = self.context['request'].user

        # 현재 비밀번호 체크
        current_password = data.get('current_password')
        if not current_password or not user.check_password(current_password):
            errors['current_password'] = ['현재 비밀번호가 올바르지 않습니다.']


        # password1: 빈 값, 길이 체크
        password1 = data.get('password1')
        if not password1 or not password1.strip():
            errors['password1'] = ['비밀번호를 입력해주세요.']
        elif len(password1) < 8:
            errors['password1'] = ['비밀번호는 8자 이상이어야 합니다.']

        # password2: 빈 값 체크
        password2 = data.get('password2')
        if not password2 or not password2.strip():
            errors['password2'] = ['비밀번호 확인을 입력해주세요.']

        # password1, password2 일치 체크 (둘 다 입력된 경우만)
        if password1 and password2 and password1 != password2:
            errors['password2'] = ['비밀번호가 일치하지 않습니다.']

        # 추가 검증 필요시 여기에...

        if errors:
            raise serializers.ValidationError(errors)

        return data
    
    def save(self, **kwargs):
        password = self.validated_data.get('password1')
        user = self.instance
        user.set_password(password)
        user.save()
        return user

