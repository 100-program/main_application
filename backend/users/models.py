from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """カスタムユーザーモデル"""
    firebase_uid = models.CharField(max_length=128, unique=True, null=True, blank=True)
    current_points = models.IntegerField(default=0)
    avatar_level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    """タスクモデル"""
    PRIORITY_CHOICES = [
        (1, '低'),
        (2, '中'),
        (3, '高'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class StudyRecord(models.Model):
    """勉強時間記録モデル"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_records')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    duration_seconds = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.duration_seconds}秒"


class Item(models.Model):
    """アイテムモデル"""
    ITEM_TYPES = [
        ('avatar', 'アバター'),
        ('music', '音楽'),
        ('theme', 'テーマ'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=ITEM_TYPES)
    cost = models.IntegerField()
    image_url = models.URLField(blank=True)
    asset_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class UserItem(models.Model):
    """ユーザーが所有するアイテムモデル"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    acquired_at = models.DateTimeField(auto_now_add=True)
    is_equipped = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'item']

    def __str__(self):
        return f"{self.user.username} - {self.item.name}"


class LevelConfig(models.Model):
    """レベル設定モデル"""
    level = models.IntegerField(unique=True)
    required_points = models.IntegerField()
    avatar_image_url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['level']

    def __str__(self):
        return f"レベル {self.level}"

