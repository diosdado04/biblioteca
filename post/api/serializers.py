from rest_framework.serializers import ModelSerializer
from post.models import Book,Author,Stock

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'