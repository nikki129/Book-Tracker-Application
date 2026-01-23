from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "status",
            "rating",
            "notes",
            "cover_url",
            "created_at",
            "updated_at",
        ]
