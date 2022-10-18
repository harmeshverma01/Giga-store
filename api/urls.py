from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product-category', views.ProductCategoryViews)
router.register('products',views.ProductView)
router.register('Customers', views.CustomerView)
router.register('delivery', views.DeliveryDetailsView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view()),
    path('carts/', views.CartView.as_view()),
    path('checkout/', views.CheckOutView.as_view()),
]


