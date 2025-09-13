from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from .models import User, Task, StudyRecord, Item, UserItem, LevelConfig
from .serializers import (
    UserSerializer, TaskSerializer, StudyRecordSerializer, 
    ItemSerializer, UserItemSerializer, LevelConfigSerializer
)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """ユーザープロフィール取得・更新"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class TaskListCreateView(generics.ListCreateAPIView):
    """タスク一覧取得・作成"""
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """タスク詳細取得・更新・削除"""
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_task(request, task_id):
    """タスク完了"""
    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.is_completed = True
        task.completed_at = timezone.now()
        task.save()
        
        # ジェム付与（1タスク = 10ジェム）
        user = request.user
        user.current_points += 10
        user.save()
        
        return Response({
            'message': 'タスクが完了しました',
            'gems_earned': 10,
            'total_gems': user.current_points
        })
    except Task.DoesNotExist:
        return Response({'error': 'タスクが見つかりません'}, status=status.HTTP_404_NOT_FOUND)


class StudyRecordListCreateView(generics.ListCreateAPIView):
    """勉強記録一覧取得・作成"""
    serializer_class = StudyRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyRecord.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_timer(request):
    """タイマー開始"""
    task_id = request.data.get('task_id')
    task = None
    if task_id:
        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'タスクが見つかりません'}, status=status.HTTP_404_NOT_FOUND)
    
    study_record = StudyRecord.objects.create(
        user=request.user,
        task=task,
        start_time=timezone.now()
    )
    
    return Response({
        'record_id': study_record.id,
        'start_time': study_record.start_time,
        'message': 'タイマーを開始しました'
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def stop_timer(request, record_id):
    """タイマー停止"""
    try:
        study_record = StudyRecord.objects.get(id=record_id, user=request.user)
        end_time = timezone.now()
        duration = (end_time - study_record.start_time).total_seconds()
        
        study_record.end_time = end_time
        study_record.duration_seconds = int(duration)
        study_record.save()
        
        # ジェム付与（1分 = 1ジェム）
        gems_earned = int(duration // 60)
        user = request.user
        user.current_points += gems_earned
        user.save()
        
        return Response({
            'duration_seconds': study_record.duration_seconds,
            'gems_earned': gems_earned,
            'total_gems': user.current_points,
            'message': 'タイマーを停止しました'
        })
    except StudyRecord.DoesNotExist:
        return Response({'error': '記録が見つかりません'}, status=status.HTTP_404_NOT_FOUND)


class ItemListView(generics.ListAPIView):
    """アイテム一覧取得"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class UserItemListView(generics.ListAPIView):
    """ユーザー所有アイテム一覧取得"""
    serializer_class = UserItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserItem.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_item(request, item_id):
    """アイテム購入"""
    try:
        item = Item.objects.get(id=item_id)
        user = request.user
        
        # ジェム不足チェック
        if user.current_points < item.cost:
            return Response({'error': 'ジェムが不足しています'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 既に所有しているかチェック
        if UserItem.objects.filter(user=user, item=item).exists():
            return Response({'error': '既に所有しているアイテムです'}, status=status.HTTP_400_BAD_REQUEST)
        
        # アイテム購入
        user.current_points -= item.cost
        user.save()
        
        user_item = UserItem.objects.create(user=user, item=item)
        
        return Response({
            'message': 'アイテムを購入しました',
            'item': ItemSerializer(item).data,
            'remaining_gems': user.current_points
        })
    except Item.DoesNotExist:
        return Response({'error': 'アイテムが見つかりません'}, status=status.HTTP_404_NOT_FOUND)


class LevelConfigListView(generics.ListAPIView):
    """レベル設定一覧取得"""
    queryset = LevelConfig.objects.all()
    serializer_class = LevelConfigSerializer
    permission_classes = [IsAuthenticated]

