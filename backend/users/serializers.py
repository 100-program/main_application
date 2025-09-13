from rest_framework import serializers
from .models import User, Task, StudyRecord, Item, UserItem, LevelConfig


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'current_points', 'avatar_level', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'is_completed', 'completed_at', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'completed_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class StudyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyRecord
        fields = ['id', 'task', 'start_time', 'end_time', 'duration_seconds', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'type', 'cost', 'image_url', 'asset_url', 'created_at']
        read_only_fields = ['id', 'created_at']


class UserItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    
    class Meta:
        model = UserItem
        fields = ['id', 'item', 'acquired_at', 'is_equipped']
        read_only_fields = ['id', 'acquired_at']


class LevelConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelConfig
        fields = ['level', 'required_points', 'avatar_image_url', 'description']

