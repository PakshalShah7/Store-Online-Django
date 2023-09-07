from django.urls import path
from category.views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView

app_name = 'category'

urlpatterns = [

    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete')

]
