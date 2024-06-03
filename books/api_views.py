from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreatorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer