from rest_framework.viewsets import ModelViewSet

# Create your views here.
from post.models import Book,Author,Stock
from post.api.serializers import BookSerializer,AuthorSerializer,StockSerializer

###filters
from django_filters.rest_framework import DjangoFilterBackend

class BookApiViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['title']
    filterset_fields = {
        'price': ['gte','lte'],
        'editorial': ['contains'],
        'title': ['exact'],
    }

class AuthorApiViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class StockApiViewSet(ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']