import firebase_admin
from firebase_admin import credentials, firestore, storage
from django.conf import settings
import os


class FirebaseClient:
    """Firebase接続クライアント"""
    
    def __init__(self):
        self._db = None
        self._bucket = None
        self._initialize_firebase()
    
    def _initialize_firebase(self):
        """Firebase初期化"""
        if not firebase_admin._apps:
            # 本番環境では環境変数から認証情報を取得
            if os.getenv('FIREBASE_CREDENTIALS_PATH'):
                cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIALS_PATH'))
            else:
                # 開発環境用のデフォルト設定
                cred = credentials.ApplicationDefault()
            
            firebase_admin.initialize_app(cred, {
                'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET', 'your-project.appspot.com')
            })
    
    @property
    def db(self):
        """Firestoreデータベースインスタンス"""
        if self._db is None:
            self._db = firestore.client()
        return self._db
    
    @property
    def bucket(self):
        """Cloud Storageバケットインスタンス"""
        if self._bucket is None:
            self._bucket = storage.bucket()
        return self._bucket


# シングルトンインスタンス
firebase_client = FirebaseClient()

