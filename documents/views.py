from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from documents.models import Document
from documents.serializers import DocumentSerializer


class DocumentView(APIView):
    serializer_class = DocumentSerializer

    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            document = serializer.save()
            return Response(DocumentSerializer(document).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetailAPI(APIView):
    serializer_class = DocumentSerializer

    def get(self, request, id):
        document = get_object_or_404(Document, id=id)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, id):
        document = get_object_or_404(Document, id=id)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        document = get_object_or_404(Document, id=id)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
