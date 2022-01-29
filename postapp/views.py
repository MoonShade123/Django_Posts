import base64
import json

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, User
from .serializer import LoginSerializer, RegistrationSerializer, PostSerializer


class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                posts = Post.objects.get(id=id)
                serializer = PostSerializer(posts)
        except:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)

        return Response({"Posts": serializer.data})

    def post(self, request):
        posts = request.data
        author = request.user
        new_post = Post.objects.create(author=author, title=posts["title"], body=posts["body"],
                                       imageUrl=posts["imageUrl"])

        new_post.save()

        serializer = PostSerializer(new_post).data

        return Response(serializer)

    def put(self, request):
        id = request.query_params["id"]
        saved_post = get_object_or_404(Post.objects.all(), id=id)

        post = request.data

        saved_post.title = post['title']
        saved_post.body = post['body']
        saved_post.imageUrl = post['imageUrl']

        saved_post.save()

        serializer = PostSerializer(saved_post)
        return Response(serializer.data)

    def delete(self, request):
        id = request.query_params["id"]
        post = get_object_or_404(Post.objects.all(), id=id)
        post.delete()
        return Response(f'Post with Id:{id} deleted successfully')


