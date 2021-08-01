

from django.urls import path
from . import views


urlpatterns=[
    path('sign_up/',views.Register,name='register'),
    path('profile/',views.Profile,name='profile'),
    path('log_out',views.LogOut,name='log_out'),
    path('add_cart/<str:pk>',views.AddCart,name='add_cart'),
    path('payment_method/<str:pk>/',views.PaymentMethod,name='payment_method'),
    path("cart_cancel/<str:pk>/",views.CancelCart,name='cancel_cart'),
    path('about_book/<str:pk>/',views.AboutBook,name='about_book'),
    path('panel/',views.AdminDashboard,name='admin_dashboard'),
    path('add_new_book/',views.AddNewBook,name='add_book'),
    path('edit_book/<str:pk>/',views.EditBookDetails,name='edit_book'),
    path('delete_book/<str:pk>/',views.DeleteBook,name='delete_book'),
    path('',views.home,name='home'),
  
    path('log_in/',views.LogIn,name='log_in'),
    path('edit_order/<str:pk>/',views.EditOrder,name='edit_order'),

]
