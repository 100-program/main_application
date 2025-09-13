from .client import firebase_client
from datetime import datetime
from typing import Dict, List, Optional


class FirestoreService:
    """Firestore操作サービス"""
    
    def __init__(self):
        self.db = firebase_client.db
    
    # ユーザー関連操作
    def create_user(self, user_data: Dict) -> str:
        """ユーザー作成"""
        doc_ref = self.db.collection('users').document()
        user_data['created_at'] = datetime.now()
        user_data['updated_at'] = datetime.now()
        doc_ref.set(user_data)
        return doc_ref.id
    
    def get_user(self, user_id: str) -> Optional[Dict]:
        """ユーザー取得"""
        doc = self.db.collection('users').document(user_id).get()
        return doc.to_dict() if doc.exists else None
    
    def update_user(self, user_id: str, user_data: Dict) -> bool:
        """ユーザー更新"""
        try:
            user_data['updated_at'] = datetime.now()
            self.db.collection('users').document(user_id).update(user_data)
            return True
        except Exception:
            return False
    
    # タスク関連操作
    def create_task(self, user_id: str, task_data: Dict) -> str:
        """タスク作成"""
        doc_ref = self.db.collection('tasks').document()
        task_data['user_id'] = user_id
        task_data['created_at'] = datetime.now()
        task_data['updated_at'] = datetime.now()
        doc_ref.set(task_data)
        return doc_ref.id
    
    def get_user_tasks(self, user_id: str) -> List[Dict]:
        """ユーザーのタスク一覧取得"""
        docs = self.db.collection('tasks').where('user_id', '==', user_id).stream()
        return [{'id': doc.id, **doc.to_dict()} for doc in docs]
    
    def update_task(self, task_id: str, task_data: Dict) -> bool:
        """タスク更新"""
        try:
            task_data['updated_at'] = datetime.now()
            self.db.collection('tasks').document(task_id).update(task_data)
            return True
        except Exception:
            return False
    
    def delete_task(self, task_id: str) -> bool:
        """タスク削除"""
        try:
            self.db.collection('tasks').document(task_id).delete()
            return True
        except Exception:
            return False
    
    # 勉強記録関連操作
    def create_study_record(self, user_id: str, record_data: Dict) -> str:
        """勉強記録作成"""
        doc_ref = self.db.collection('study_records').document()
        record_data['user_id'] = user_id
        record_data['created_at'] = datetime.now()
        doc_ref.set(record_data)
        return doc_ref.id
    
    def get_user_study_records(self, user_id: str) -> List[Dict]:
        """ユーザーの勉強記録一覧取得"""
        docs = self.db.collection('study_records').where('user_id', '==', user_id).stream()
        return [{'id': doc.id, **doc.to_dict()} for doc in docs]
    
    # アイテム関連操作
    def get_items(self) -> List[Dict]:
        """アイテム一覧取得"""
        docs = self.db.collection('items').stream()
        return [{'id': doc.id, **doc.to_dict()} for doc in docs]
    
    def create_user_item(self, user_id: str, item_id: str) -> str:
        """ユーザーアイテム作成"""
        doc_ref = self.db.collection('user_items').document()
        data = {
            'user_id': user_id,
            'item_id': item_id,
            'acquired_at': datetime.now(),
            'is_equipped': False
        }
        doc_ref.set(data)
        return doc_ref.id
    
    def get_user_items(self, user_id: str) -> List[Dict]:
        """ユーザー所有アイテム一覧取得"""
        docs = self.db.collection('user_items').where('user_id', '==', user_id).stream()
        return [{'id': doc.id, **doc.to_dict()} for doc in docs]


# シングルトンインスタンス
firestore_service = FirestoreService()

