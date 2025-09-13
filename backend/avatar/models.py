from django.db import models
from users.models import User


class AvatarModel(models.Model):
    """3Dアバターモデル"""
    name = models.CharField(max_length=100)
    glb_file_url = models.URLField()
    thumbnail_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    unlock_level = models.IntegerField(default=1)
    gem_cost = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AvatarCustomization(models.Model):
    """ユーザーのアバターカスタマイズ設定"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar_customization')
    current_avatar = models.ForeignKey(AvatarModel, on_delete=models.SET_NULL, null=True, blank=True)
    current_theme_color = models.CharField(max_length=7, default='#667eea')  # HEXカラー
    current_music = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}のカスタマイズ"


class ThemeColor(models.Model):
    """テーマカラー"""
    name = models.CharField(max_length=50)
    primary_color = models.CharField(max_length=7)  # HEXカラー
    secondary_color = models.CharField(max_length=7)  # HEXカラー
    accent_color = models.CharField(max_length=7)  # HEXカラー
    gem_cost = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BackgroundMusic(models.Model):
    """BGM"""
    name = models.CharField(max_length=100)
    file_url = models.URLField()
    duration_seconds = models.IntegerField()
    gem_cost = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

