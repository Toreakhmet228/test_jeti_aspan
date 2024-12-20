from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from main_func.models import Product, Store, CustomUser, City
from main_func.serializers import ProductSerializer, ProductDetailSerializer, StoreSerializer, ProductImageSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        city_id = self.request.query_params.get('city_id')
        store_id = self.request.query_params.get('store_id')

        if city_id:
            queryset = queryset.filter(city__id=city_id)
        if store_id:
            queryset = queryset.filter(store__id=store_id)

        return queryset


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increment_view_count()  # Increment view count every time the product is viewed
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StoreListView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]


class ProductSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query', '')
        city_id = request.query_params.get('city_id')

        products = Product.objects.filter(name__icontains=query)

        if city_id:
            products = products.filter(city__id=city_id)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class UpdateStocksView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        updates = request.data.get('updates', [])

        for update in updates:
            try:
                product = Product.objects.get(id=update['id'])
                product.stock = update['stock']
                product.save()
            except Product.DoesNotExist:
                return Response({"error": f"Product with id {update['id']} does not exist."},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Stocks updated successfully."}, status=status.HTTP_200_OK)




