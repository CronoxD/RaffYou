
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Views
from carts import views

router = routers.DefaultRouter()
router.register('products', views.CartProductViewSet)

app_name = 'carts'


urlpatterns = [
    path('', views.cart_view, name='index'),
    path('api/', include(router.urls)),
]
