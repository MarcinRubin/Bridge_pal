from rest_framework import serializers

from .models import Profile, User


def validate_username(value):
    if User.objects.filter(username=value).exists():
        raise serializers.ValidationError("User with this username already exists!")
    return value


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "confirm_password"]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError(
                "Password is different from the confirm password!"
            )
        return attrs

    def create(self, validated_data):
        user_obj = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        user_obj.is_active = True
        user_obj.save()
        return user_obj


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
