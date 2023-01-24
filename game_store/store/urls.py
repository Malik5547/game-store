from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('logout', views.log_out, name='logout'),
    path('cat/<int:cat_id>', views.category, name='category'),
    path('product/<int:product_id>', views.product, name='category'),
    # path('product/<int:product_id>', views.purchase, name='purchase'),
    path('<int:product_id>', views.product, name='product'),
]