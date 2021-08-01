from django.urls import path
from .consumers import *

ws_urlpatterns=[
    path('ws/about_book/<str:book_name>/<str:pk>/',BookCommentConsumer.as_asgi()),
    path('ws/cart_add/',CartAddConsumer.as_asgi()),
    
]

# path('ws/edit_order/',EditOrderConsumer.as_asgi())