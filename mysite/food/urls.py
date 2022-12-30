from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
      #food/
      #path('', views.index, name='index'),
      path('', views.IndexClassView.as_view(), name='index'),
      #food/1
      path('<int:pk>/', views.DetailsClassView.as_view(), name='details'),
      # path('<int:item_id>/', views.details, name='details'),
      path('item/', views.item, name='item'),
      #add item
      #path('add', views.create_item, name='create_item'),
      path('add', views.CreateItemView.as_view(), name='create_item'),
      #edit item
      path('update/<int:id>', views.update_item, name='update_item'),
      #delete item
      #path('itemlist/<int:id>', views.delete_item_list, name='delete_item_list'),
      path('delete/<int:id>', views.delete_item, name='delete_item'),
] 