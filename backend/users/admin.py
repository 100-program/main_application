from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Task, StudyRecord, Item, UserItem, LevelConfig


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'current_points', 'avatar_level', 'created_at']
    list_filter = ['avatar_level', 'created_at']
    search_fields = ['username', 'email']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('追加情報', {'fields': ('firebase_uid', 'current_points', 'avatar_level')}),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'priority', 'is_completed', 'due_date', 'created_at']
    list_filter = ['priority', 'is_completed', 'created_at']
    search_fields = ['title', 'user__username']
    date_hierarchy = 'created_at'


@admin.register(StudyRecord)
class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'duration_seconds', 'start_time', 'end_time']
    list_filter = ['created_at']
    search_fields = ['user__username', 'task__title']
    date_hierarchy = 'created_at'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'cost', 'created_at']
    list_filter = ['type', 'created_at']
    search_fields = ['name']


@admin.register(UserItem)
class UserItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'is_equipped', 'acquired_at']
    list_filter = ['is_equipped', 'item__type', 'acquired_at']
    search_fields = ['user__username', 'item__name']


@admin.register(LevelConfig)
class LevelConfigAdmin(admin.ModelAdmin):
    list_display = ['level', 'required_points', 'description']
    ordering = ['level']

