from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.reverse_related import ManyToManyRel
from django.template import *
from django.template.defaultfilters import default



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=60, null=True)
    photo = models.ImageField(default='avatar.png', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300, null=True,default=' ')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=2200, null=True, blank=True)
    photo = models.ImageField(default='avatar.png', null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=800, null=True, blank=True)
    def __str__(self):
        return self.name

class Catagory(models.Model):
    name=CharField(max_length=50,null=True)
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, null=True)
    type = models.ForeignKey(Catagory,null=True,on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=1500, null=True)
    reating = models.FloatField(null=True,blank=True,default=0)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.CASCADE, blank=True)
    cover = models.ImageField(default='defaultcover.jpg',null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1200, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.customer.name+"("+self.book.name+")"

class CommentReply(models.Model):
    comment=models.ForeignKey(Review,null=True,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    reply = models.CharField(max_length=1200, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.comment.customer.name+"("+self.comment.book.name+")"

class Paymethod(models.Model):
    name=models.CharField(max_length=50,null=True)
    account=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATTUS = (
        ('Pending', 'Pending'),
        ('Delevered', 'Delevered'),
        ('On the way', 'On the way')
    )
    PAY_STATTUS=(
        ("Paid","Paid"),("Due","Due")
    )
    
    product = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    shipment_address=models.CharField(max_length=300,null=True,default=" ")
    stattus = models.CharField(max_length=50, null=True, default='Pending', choices=STATTUS)
    pay_method=models.ForeignKey(Paymethod,null=True,on_delete=models.CASCADE)
    pay_stattus=models.CharField(max_length=50,null=True,choices=PAY_STATTUS)
    time_created=models.DateTimeField(auto_now_add=True)
    estimated_date=models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.customer.name + " + " + self.product.name+" + "+self.customer.address


class Cart(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.customer.name+"("+self.book.name+")"

class Icons(models.Model):
    name=models.CharField(max_length=200,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='icons/')

    def __str__(self):
        return self.name

