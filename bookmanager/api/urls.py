from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .controllers import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('books', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
