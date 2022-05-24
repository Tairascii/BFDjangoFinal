from rest_framework import serializers

from core.models import Book, Journal, BookJournal


class BookJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournal
        fields = ('id', 'name', 'price', 'description', 'created_at')


class BookSerializer(BookJournalSerializer):
    class Meta:
        model = Book
        fields = BookJournalSerializer.Meta.fields + ('num_pages', 'genre')


class JournalSerializer(BookJournalSerializer):
    class Meta:
        model = Journal
        fields = BookJournalSerializer.Meta.fields + ('type', 'publisher')
