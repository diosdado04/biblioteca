from rest_framework.routers import DefaultRouter
from post.api.views import BookApiViewSet,AuthorApiViewSet,StockApiViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='book', basename='book', viewset=BookApiViewSet)
router_posts.register(prefix='author', basename='author', viewset=AuthorApiViewSet)
router_posts.register(prefix='stock', basename='stock', viewset=StockApiViewSet)
