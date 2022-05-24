from django.shortcuts import render
import json

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.models import Book, Journal

from core.serializers import BookSerializer, JournalSerializer
# Create your views here.


class BookViewSet(viewsets.ViewSet):
    def get_query(self):
        return Book.objects.all()

    def list(self, request):
        serializer = BookSerializer(self.get_query(), many=True)
        return Response(serializer.data)

    def create(self, request):
        data = json.loads(request.body)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=200)


class BookDetailViewSet(viewsets.ViewSet):
    def partial_update(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser,)


class JournalViewSet(viewsets.ViewSet):
    def get_query(self):
        return Journal.objects.all()

    def list(self, request):
        serializer = JournalSerializer(self.get_query(), many=True)
        return Response(serializer.data)

    def create(self, request):
        data = json.loads(request.body)
        serializer = JournalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=200)


class JournalDetailViewSet(viewsets.ViewSet):
    def partial_update(self, request, pk=None):
        journal = Journal.objects.get(id=pk)
        serializer = JournalSerializer(instance=journal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        journal = Journal.objects.get(id=pk)
        journal.delete()
        return Response({'message': 'deleted'}, status=204)

    permission_classes = (IsAdminUser,)
