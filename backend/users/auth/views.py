from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from ..models import User as CustomUser
from ..serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """ユーザー登録"""
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    firebase_uid = request.data.get('firebase_uid')
    
    if not all([username, email, password]):
        return Response({'error': '必要な情報が不足しています'}, status=status.HTTP_400_BAD_REQUEST)
    
    if CustomUser.objects.filter(username=username).exists():
        return Response({'error': 'ユーザー名が既に使用されています'}, status=status.HTTP_400_BAD_REQUEST)
    
    if CustomUser.objects.filter(email=email).exists():
        return Response({'error': 'メールアドレスが既に使用されています'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password,
        firebase_uid=firebase_uid
    )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'user': UserSerializer(user).data,
        'token': token.key,
        'message': 'ユーザー登録が完了しました'
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """ログイン"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not all([username, password]):
        return Response({'error': 'ユーザー名とパスワードが必要です'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'ログインしました'
        })
    else:
        return Response({'error': 'ユーザー名またはパスワードが正しくありません'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout(request):
    """ログアウト"""
    try:
        request.user.auth_token.delete()
        return Response({'message': 'ログアウトしました'})
    except:
        return Response({'error': 'ログアウトに失敗しました'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def firebase_auth(request):
    """Firebase認証"""
    firebase_uid = request.data.get('firebase_uid')
    email = request.data.get('email')
    username = request.data.get('username')
    
    if not firebase_uid:
        return Response({'error': 'Firebase UIDが必要です'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # 既存ユーザーを検索
        user = CustomUser.objects.get(firebase_uid=firebase_uid)
    except CustomUser.DoesNotExist:
        # 新規ユーザー作成
        if not all([email, username]):
            return Response({'error': 'メールアドレスとユーザー名が必要です'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            firebase_uid=firebase_uid
        )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'user': UserSerializer(user).data,
        'token': token.key,
        'message': 'Firebase認証が完了しました'
    })

