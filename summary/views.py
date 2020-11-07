from rest_framework import generics, serializers
from rest_framework.response import Response

from .models import Summary


class SummaryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Summary
        fields = ('thumbnail', 'id', 'author', 'section_name', 'category_name', 'summary_name', 'url', 'created_date')


class SummaryListView(generics.ListAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummaryListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)