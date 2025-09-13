from django.contrib import admin
from .models import AvatarModel, AvatarCustomization, ThemeColor, BackgroundMusic


@admin.register(AvatarModel)
class AvatarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'unlock_level', 'gem_cost', 'created_at']
    list_filter = ['unlock_level', 'created_at']
    search_fields = ['name', 'description']


@admin.register(AvatarCustomization)
class AvatarCustomizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'current_avatar', 'current_theme_color', 'updated_at']
    list_filter = ['updated_at']
    search_fields = ['user__username']


@admin.register(ThemeColor)
class ThemeColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'primary_color', 'gem_cost', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(BackgroundMusic)
class BackgroundMusicAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_seconds', 'gem_cost', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']

