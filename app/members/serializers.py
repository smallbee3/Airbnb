from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # 3/31 password 가려야함.
        # field = (
        #     'pk',
        #     # 'username',
        #     'email',
        #     'name',
        #     'img_profile',
        #     'phone_num',
        #
        #     # 'is_host',
        #     # 'is_facebookuser',
        # )

    # 방법 1 - 블로그 참고 (일일이 전부 저장해줄 수 없는 문제?)
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username=validated_data.get('email'),
    #         email=validated_data.get('email'),
    #         password=validated_data.get('password'),
    #     )
    #     return user

    # 방법 2 - super() 사용
    # def create(self, validated_data):
    #     user = super().create(validated_data)
    #     user.username = validated_data.get('email')
    #     user.password = validated_data.get('password')
    #     user.save()
    #     return user

    # 방법 3 - https://stackoverflow.com/questions/42258777/invalid-password-format-or-unknown-hashing-algorithm-django-create-view-user
    #           비밀번호 유효성검사를 안하는 문제( ex. 1입력가능 )
    # def create(self, validated_data):
    #     user = super().create(validated_data)
    #     user.username = validated_data.get('email')
    #     user.set_password(validated_data.get('password'))
    #     user.save()
    #     return user

    # 방법 5 - 포기
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('email'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            name=validated_data.get('name'),
            img_profile=validated_data.get('img_profile'),
            phone_num=validated_data.get('phone_num', None),
            is_host=validated_data.get('is_host', False),
            is_facebookuser=validated_data.get('is_facebookuser', False),
        )
        # user = super().update(user, validated_data)
        return user
