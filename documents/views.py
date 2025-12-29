from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from documents.models import Document
from documents.serializers import DocumentSerializer


class DocumentView(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = [IsAuthenticated]
