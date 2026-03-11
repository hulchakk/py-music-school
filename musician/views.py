from rest_framework.viewsets import ModelViewSet

from musician.serializers import (
    MusicianSerializer,
    MusicianGetSerializer,
    Musician,
)


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return MusicianGetSerializer

        return MusicianSerializer
