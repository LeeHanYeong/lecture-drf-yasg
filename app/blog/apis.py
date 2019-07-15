from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostCreateSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostListCreateAPIView(APIView):
    def get(self, request):
        # Post모델의 QuerySet을
        posts = Post.objects.all()
        # PostSerializer를 사용해 직렬화 (many=True옵션으로 multiple objects대응)
        serializer = PostSerializer(posts, many=True)
        # Serializer의 data를 Response객체 생성의 인수로 사용
        response = Response(serializer.data)
        # 만들어진 Response객체를 리턴
        return response

    def post(self, request):
        # 새 Post를 작성
        # author는 request.user를 사용

        # request.data에 데이터가 전달됨
        # 전달받은 데이터를 data키워드인수로 PostSerializer생성에 전달, serializer생성
        serializer = PostCreateSerializer(data=request.data)

        # serializer.is_valid() 호출로 validation점검
        if serializer.is_valid():
            # valid하다면, serializer.save()를 호출해서 ModelSerializer로 DB row생성
            #  -> 이 과정에서, save()에 author를 request.user로 전달
            instance = serializer.save(author=request.user)
            return Response(PostSerializer(instance).data)
        else:
            # valid하지 않다면, Response에 serializers.errors를 전달
            return Response(serializer.errors)
