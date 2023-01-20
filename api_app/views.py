
from rest_framework import viewsets
from .serializers import CartItemSerializer
from .models import CartItem
from rest_framework.response import Response


class CartItemViews(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


    def update(self, request, *args, **kwargs):
        response = super(CartItemViews, self).update(request, *args, **kwargs)
        # Your override
        return Response({"status": "success", "data": response.data})
