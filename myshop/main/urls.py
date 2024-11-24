from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index_view'),
    path('catalog/', views.catalog, name='catalog_view'),
    path('contacts/', views.contacts, name='contacts_view'),
    path('catalog/<int:pk>', views.ProductDetaiView.as_view(), name="product-detail"),
    path('baskets/add/<int:product_id>', basket_add , name="basket_add"),
    path('users/', include('users.urls', namespace='users')),
    path('baskets/remove/<int:basket_id>', basket_remove , name="basket_remove"),
    path('order_create', views.order_create, name='order_create' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



