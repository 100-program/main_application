from django.urls import path
from . import views

urlpatterns = [
    # アバター関連
    path('models/', views.AvatarModelListView.as_view(), name='avatar-model-list'),
    path('customization/', views.AvatarCustomizationView.as_view(), name='avatar-customization'),
    path('change/<int:avatar_id>/', views.change_avatar, name='change-avatar'),
    
    # テーマカラー関連
    path('themes/', views.ThemeColorListView.as_view(), name='theme-color-list'),
    path('themes/<int:theme_id>/change/', views.change_theme_color, name='change-theme-color'),
    
    # BGM関連
    path('music/', views.BackgroundMusicListView.as_view(), name='background-music-list'),
    path('music/<int:music_id>/change/', views.change_background_music, name='change-background-music'),
]

