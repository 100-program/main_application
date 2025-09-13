from rest_framework import serializers
from .models import AvatarModel, AvatarCustomization, ThemeColor, BackgroundMusic


class AvatarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvatarModel
        fields = ['id', 'name', 'glb_file_url', 'thumbnail_url', 'description', 'unlock_level', 'gem_cost', 'created_at']


class AvatarCustomizationSerializer(serializers.ModelSerializer):
    current_avatar = AvatarModelSerializer(read_only=True)
    
    class Meta:
        model = AvatarCustomization
        fields = ['id', 'current_avatar', 'current_theme_color', 'current_music', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ThemeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeColor
        fields = ['id', 'name', 'primary_color', 'secondary_color', 'accent_color', 'gem_cost', 'created_at']


class BackgroundMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundMusic
        fields = ['id', 'name', 'file_url', 'duration_seconds', 'gem_cost', 'created_at']

