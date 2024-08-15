from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from .serializers import BookSerializer
from .services import BookService
from drf_spectacular.utils import extend_schema

class BookListCreateView(ListCreateAPIView):
    @extend_schema(tags=["Books"])
    def get(self, request, *args, **kwargs):
        service = BookService(request)
        try:
            books = service.list_books()
            serializer = BookSerializer(books, many=True)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(tags=["Books"])
    def post(self, request, *args, **kwargs):
        service = BookService(request)
        try:
            book = service.create_book()
            serializer = BookSerializer(book)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"success": False, "message": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    @extend_schema(tags=["Books"])
    def get(self, request, pk, *args, **kwargs):
        service = BookService(request)
        try:
            book = service.retrieve_book(pk)
            serializer = BookSerializer(book)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(tags=["Books"])
    def put(self, request, pk, *args, **kwargs):
        service = BookService(request)
        try:
            book = service.update_book(pk)
            serializer = BookSerializer(book)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"success": False, "message": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(tags=["Books"])
    def delete(self, request, pk, *args, **kwargs):
        service = BookService(request)
        try:
            service.delete_book(pk)
            return Response({"success": True, "message": "Book deleted successfully"}, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"success": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

