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

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('email'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
        )
        return user

