from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>', views.product, name='product'),
]