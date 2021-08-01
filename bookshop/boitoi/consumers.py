from channels.auth import get_user
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *
from asgiref.sync import sync_to_async,async_to_sync
import asyncio
from datetime import datetime
from django.utils import timezone
import base64 as base
from.forms import *

class BookCommentConsumer(WebsocketConsumer):
    def save_data(self,data):
        user=Customer.objects.get(name=data['customer'])
        Review.objects.create(customer=user,book=Book.objects.get(id=data['book']),comment=data['comment'])
        
    def get_photo(self,data):
        user=Customer.objects.get(name=data)
        return user.photo

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )



    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        comment = text_data_json['comment']
        user=str(self.scope['user'])
        now = timezone.now()
        photo=self.get_photo(user)
        photo=photo.read()
        self.save_data({
            'customer':user,
            'book':text_data_json['pk'],
            'comment':comment
        })
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
            'type': 'chat_message',
            'user':user,
            'comment':comment,
            'time':str(now),
            'photo':base.b64encode(photo).decode('utf-8'),
                
            }
        )
    
    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
       
class CartAddConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def receive(self, text_data=None, bytes_data=None):
        received_data=json.loads(text_data)
        user=Customer.objects.get(name=received_data['user'])
        book=Book.objects.get(id=received_data['book_id'])
        Cart.objects.create(customer=user,book=book)
        book_cover=book.cover
        book_cover=book_cover.read()
        send_data=json.dumps({
            'book_name':book.name,
            'book_author':book.author.name,
            'book_price':book.price,
            'book_cover':base.b64encode(book_cover).decode('utf-8'),
            'book_id':received_data['book_id'],
        })
 
        self.send(text_data=send_data)
        
'''

class EditOrderConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self,text_data=None,bytes_data=None):
        received_data=json.loads(text_data)
        print(received_data)
        order=Order.objects.get(id=received_data['id'])
        book_cover=order.product.cover
        book_cover=book_cover.read()
        book_cover=base.b64encode(book_cover).decode('utf-8')
        send_data=json.dumps({
            'order_id':order.id,
            'customer_name':order.customer.name,
            'book_name':order.product.name,
            'book_cover':book_cover,
            'stattus':order.stattus,
            'pay_method':order.pay_method.name,
            'pay_stattus':order.pay_stattus,
            'shipment_address':order.shipment_address,
        })
        self.send(text_data=send_data)
'''
