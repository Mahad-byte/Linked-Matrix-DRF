from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPI(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        comment = get_object_or_404(Comment, id=id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id):
        comment = get_object_or_404(Comment, id=id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = get_object_or_404(Comment, id=id)
        comment.delete()
        return Response("Deleted!!", status=status.HTTP_200_OK)
