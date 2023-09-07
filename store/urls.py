from django.urls import path
from store.views import Index, StoreCreateView, StoreUpdateView, ImageCreateView, ImageDeleteView, \
    StoreListView, MyStoreListView, StoreDeleteView, StoreDetailView

app_name = 'store'

urlpatterns = [

    path('index/', Index.as_view(), name='index'),
    path('image/create/', ImageCreateView.as_view(), name='image_create'),
    path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='image_delete'),
    path('store/create/', StoreCreateView.as_view(), name='store_create'),
    path('store/update/<int:pk>/', StoreUpdateView.as_view(), name='store_update'),
    path('store/list/', StoreListView.as_view(), name='store_list'),
    path('my-store/list/', MyStoreListView.as_view(), name='my_store_list'),
    path('store/detail/<int:pk>/', StoreDetailView.as_view(), name='store_detail'),
    path('store/delete/<int:pk>/', StoreDeleteView.as_view(), name='store_delete'),

]
