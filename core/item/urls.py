from django.urls import path
from .import views

app_name='item'

urlpatterns = [
    path('<int:pk>',views.detail,name='detail'),
    path('Add_item/',views.Add_item,name='Add_item'),
    path('<int:pk>/delete/',views.delete_item,name='delete'),
    path('<int:pk>/edit/',views.edit_item,name='edit'),
    path('',views.search_items,name='search'),
]
