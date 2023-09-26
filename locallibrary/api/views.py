from rest_framework import generics
from . import serializers
from .models import Cinema
from .parser import check_table_exits


class CinemaList(generics.ListAPIView):
    check_table_exits()
    queryset = Cinema.objects.all()
    serializer_class = serializers.CinemaSerializer


class CinemaDetail(generics.RetrieveAPIView):
    check_table_exits()
    queryset = Cinema.objects.all()
    serializer_class = serializers.CinemaSerializer
