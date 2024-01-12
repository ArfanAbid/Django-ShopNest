from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>',views.detail,name='detail'),
    path('Add_item/',views.Add_item,name='Add_item'),
]
