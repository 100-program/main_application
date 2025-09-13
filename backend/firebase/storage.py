from .client import firebase_client
from typing import Optional
import uuid


class StorageService:
    """Firebase Storage操作サービス"""
    
    def __init__(self):
        self.bucket = firebase_client.bucket
    
    def upload_file(self, file_data: bytes, file_name: str, content_type: str = 'application/octet-stream') -> Optional[str]:
        """ファイルアップロード"""
        try:
            # ユニークなファイル名を生成
            unique_filename = f"{uuid.uuid4()}_{file_name}"
            blob = self.bucket.blob(unique_filename)
            
            # ファイルアップロード
            blob.upload_from_string(file_data, content_type=content_type)
            
            # 公開URLを取得
            blob.make_public()
            return blob.public_url
        except Exception as e:
            print(f"ファイルアップロードエラー: {e}")
            return None
    
    def upload_glb_model(self, file_data: bytes, model_name: str) -> Optional[str]:
        """GLBモデルファイルアップロード"""
        return self.upload_file(file_data, f"{model_name}.glb", 'model/gltf-binary')
    
    def upload_image(self, file_data: bytes, image_name: str, image_type: str = 'png') -> Optional[str]:
        """画像ファイルアップロード"""
        content_type = f'image/{image_type}'
        return self.upload_file(file_data, f"{image_name}.{image_type}", content_type)
    
    def upload_audio(self, file_data: bytes, audio_name: str, audio_type: str = 'mp3') -> Optional[str]:
        """音声ファイルアップロード"""
        content_type = f'audio/{audio_type}'
        return self.upload_file(file_data, f"{audio_name}.{audio_type}", content_type)
    
    def delete_file(self, file_url: str) -> bool:
        """ファイル削除"""
        try:
            # URLからファイル名を抽出
            file_name = file_url.split('/')[-1]
            blob = self.bucket.blob(file_name)
            blob.delete()
            return True
        except Exception as e:
            print(f"ファイル削除エラー: {e}")
            return False


# シングルトンインスタンス
storage_service = StorageService()

