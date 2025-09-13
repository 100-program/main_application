from django.urls import path
from . import views

urlpatterns = [
    # ユーザー関連
    path('me/', views.UserProfileView.as_view(), name='user-profile'),
    
    # タスク関連
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='complete-task'),
    
    # 勉強記録関連
    path('study-records/', views.StudyRecordListCreateView.as_view(), name='study-record-list-create'),
    path('timer/start/', views.start_timer, name='start-timer'),
    path('timer/stop/<int:record_id>/', views.stop_timer, name='stop-timer'),
    
    # アイテム関連
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('my-items/', views.UserItemListView.as_view(), name='user-item-list'),
    path('items/<int:item_id>/purchase/', views.purchase_item, name='purchase-item'),
    
    # レベル設定
    path('level-configs/', views.LevelConfigListView.as_view(), name='level-config-list'),
]

