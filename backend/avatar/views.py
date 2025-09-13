from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import AvatarModel, AvatarCustomization, ThemeColor, BackgroundMusic
from .serializers import (
    AvatarModelSerializer, AvatarCustomizationSerializer, 
    ThemeColorSerializer, BackgroundMusicSerializer
)


class AvatarModelListView(generics.ListAPIView):
    """利用可能なアバターモデル一覧"""
    queryset = AvatarModel.objects.all()
    serializer_class = AvatarModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return AvatarModel.objects.filter(unlock_level__lte=user.avatar_level)


class AvatarCustomizationView(generics.RetrieveUpdateAPIView):
    """ユーザーのアバターカスタマイズ設定"""
    serializer_class = AvatarCustomizationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        customization, created = AvatarCustomization.objects.get_or_create(
            user=self.request.user
        )
        return customization


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_avatar(request, avatar_id):
    """アバター変更"""
    try:
        avatar = AvatarModel.objects.get(id=avatar_id)
        user = request.user
        
        # レベル制限チェック
        if avatar.unlock_level > user.avatar_level:
            return Response({'error': 'レベルが不足しています'}, status=status.HTTP_400_BAD_REQUEST)
        
        # ジェム不足チェック（有料アバターの場合）
        if avatar.gem_cost > 0 and user.current_points < avatar.gem_cost:
            return Response({'error': 'ジェムが不足しています'}, status=status.HTTP_400_BAD_REQUEST)
        
        # アバター変更
        customization, created = AvatarCustomization.objects.get_or_create(user=user)
        
        # 有料アバターの場合はジェムを消費
        if avatar.gem_cost > 0:
            user.current_points -= avatar.gem_cost
            user.save()
        
        customization.current_avatar = avatar
        customization.save()
        
        return Response({
            'message': 'アバターを変更しました',
            'avatar': AvatarModelSerializer(avatar).data,
            'remaining_gems': user.current_points
        })
    except AvatarModel.DoesNotExist:
        return Response({'error': 'アバターが見つかりません'}, status=status.HTTP_404_NOT_FOUND)


class ThemeColorListView(generics.ListAPIView):
    """テーマカラー一覧"""
    queryset = ThemeColor.objects.all()
    serializer_class = ThemeColorSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_theme_color(request, theme_id):
    """テーマカラー変更"""
    try:
        theme = ThemeColor.objects.get(id=theme_id)
        user = request.user
        
        # ジェム不足チェック
        if user.current_points < theme.gem_cost:
            return Response({'error': 'ジェムが不足しています'}, status=status.HTTP_400_BAD_REQUEST)
        
        # テーマカラー変更
        customization, created = AvatarCustomization.objects.get_or_create(user=user)
        
        user.current_points -= theme.gem_cost
        user.save()
        
        customization.current_theme_color = theme.primary_color
        customization.save()
        
        return Response({
            'message': 'テーマカラーを変更しました',
            'theme': ThemeColorSerializer(theme).data,
            'remaining_gems': user.current_points
        })
    except ThemeColor.DoesNotExist:
        return Response({'error': 'テーマカラーが見つかりません'}, status=status.HTTP_404_NOT_FOUND)


class BackgroundMusicListView(generics.ListAPIView):
    """BGM一覧"""
    queryset = BackgroundMusic.objects.all()
    serializer_class = BackgroundMusicSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_background_music(request, music_id):
    """BGM変更"""
    try:
        music = BackgroundMusic.objects.get(id=music_id)
        user = request.user
        
        # ジェム不足チェック
        if user.current_points < music.gem_cost:
            return Response({'error': 'ジェムが不足しています'}, status=status.HTTP_400_BAD_REQUEST)
        
        # BGM変更
        customization, created = AvatarCustomization.objects.get_or_create(user=user)
        
        user.current_points -= music.gem_cost
        user.save()
        
        customization.current_music = music.file_url
        customization.save()
        
        return Response({
            'message': 'BGMを変更しました',
            'music': BackgroundMusicSerializer(music).data,
            'remaining_gems': user.current_points
        })
    except BackgroundMusic.DoesNotExist:
        return Response({'error': 'BGMが見つかりません'}, status=status.HTTP_404_NOT_FOUND)

