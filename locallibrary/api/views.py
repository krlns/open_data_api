from rest_framework import generics
from . import serializers
from .models import Cinema
from .parser import parse_and_adding


def check_db():
    if not Cinema.objects.exists():
        parse_and_adding()


class CinemaList(generics.ListAPIView):
    check_db()
    queryset = Cinema.objects.all()
    serializer_class = serializers.CinemaSerializer


class CinemaDetail(generics.RetrieveAPIView):
    check_db()
    queryset = Cinema.objects.all()
    serializer_class = serializers.CinemaSerializer
