from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from media_app.api.serializers.media import MediaFileSerializer
from media_app.models import MediaFile


class MediaFileViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    serializer_class = MediaFileSerializer
    queryset = MediaFile.objects.all()