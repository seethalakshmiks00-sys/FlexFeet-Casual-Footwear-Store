from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('buy/', views.buy, name='buy'),
    path('cancel/', views.cancel_order, name='cancel'),
    path('reviews/', views.reviews, name='reviews'),
    path('add-review/', views.add_review, name='add_review'),
               path('read', views.read, name='read'),
               path('single-product/<int:pk>',views.single_profile,name='single_product'),
               path('delete-product/<int:pk>',views.delete_profile,name='delete_product'),
               path('edit-product/<int:pk>',views.edit_product,name='edit_product'),

path('',views.register,name='register'),
path('login/',views.login_view,name='login'),
path('logout/',views.logout_view,name='logout'),


]
