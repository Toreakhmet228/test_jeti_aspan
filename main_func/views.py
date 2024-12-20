from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Product
from main_func.serializers import ProductDetailSerializer


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("id")

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        product.increment_view_count()

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class ProductSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = request.query_params.get("q", "")  # Текстовый запрос для поиска
        city_id = request.query_params.get("city_id")  # id города для фильтрации

        products = Product.objects.filter(name__icontains=query, stock__gt=0)
        if city_id:
            products = products.filter(city_id=city_id)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class UpdateStockView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        new_stock = request.data.get("stock")

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        # Обновляем остатки товара
        product.stock = new_stock
        product.save()

        # Возвращаем успешный ответ
        return Response({"status": "Stock updated successfully."})