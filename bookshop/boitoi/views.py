
from boitoi.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, logout, authenticate
from .decoretors import *

from django.contrib.postgres.search import *


page_url=[]
def home(request):
    catagory=Catagory.objects.all()
    books=Book.objects.order_by("date_created").reverse()
    book_catagory=[]
    cart_count=0
    cart=None
    if request.user.is_authenticated:
        cart_count=request.user.customer.cart_set.all().count()
        cart=request.user.customer.cart_set.order_by("date_created").reverse()

    for i in catagory:
        book_list=i.book_set.order_by("date_created").reverse()
        book_catagory.append(book_list)
    context={
        'catagory':catagory,
        'all_books':books,
        'book_catagory':book_catagory,
        'cart_count':cart_count,
        'carts':cart,
    }
    return render(request, 'boitoi/home.html',context)


@authenticated_user
def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Wrong username or password')

    return render(request, 'boitoi/log_in.html')


@authenticated_user
def Register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('log_in')
    context = {
        'form': form,
    }
    return render(request, 'boitoi/register.html', context)



def Profile(request):
    user=request.user
    orders=user.customer.order_set.all()
    cart=request.user.customer.cart_set.all().reverse()
    cart_count=request.user.customer.cart_set.all().count()
    request.get_full_path()
    context={
        'total_order':orders.count(),
        'pending_order':user.customer.order_set.filter(stattus='Pending').count(),
        'delevered':user.customer.order_set.filter(stattus='Delevered').count(),
        'on_the_way':user.customer.order_set.filter(stattus='On the way').count(),
        'orders':orders,
        'carts':cart,
        'cart_count':cart_count,

    }
    return render(request,'boitoi/profile.html',context)

def LogOut(request):
    logout(request)
    return redirect('log_in')
def AddCart(request,pk):
    product=Book.objects.get(id=pk)
    user=request.user.customer
    Cart.objects.create(book=product,customer=user)
    return redirect("/") 

def PaymentMethod(request,pk):
    cart=Cart.objects.get(id=pk)
    Order.objects.create(product=cart.book,customer=cart.customer,stattus="Pending")
    print(page_url)
    cart.delete()
    return redirect('/')

def CancelCart(request,pk):
    cart=Cart.objects.get(id=pk)
    cart.delete()
    return redirect('/')


def AboutBook(request,pk):
    book=Book.objects.get(id=pk)
    user=request.user.customer
    cart=request.user.customer.cart_set.all().reverse()
    cart_count=request.user.customer.cart_set.all().count()
    comments=book.review_set.all()
    customer_all=Customer()
    context={
        'book':book,
        'carts':cart,
        'cart_count':cart_count,
        'comments':comments,
        'page_path':request.path,
        'customer_all':customer_all,
    }
    print(request.path)
    #print(request.absolute_path)
    
    
    return render(request,'boitoi/book_detail.html',context)


def AdminDashboard(request):
    orders=Order.objects.all()
    if request.user.is_authenticated:
        cart_count=request.user.customer.cart_set.all().count()
        cart=request.user.customer.cart_set.all().reverse()

    context={
        'cart_count':cart_count,
        'carts':cart,
        'all_order':orders.count(),
        'delevered_order':Order.objects.filter(stattus='Delevered').count(),
        'pending_order':Order.objects.filter(stattus='Pending').count(),
        'on_the_way_order':Order.objects.filter(stattus='On the way').count(),
        'orders':orders.reverse()
    }

    return render(request,'boitoi/admin_dashboard.html',context)



    #add new book
def AddNewBook(request):
    book_form=NewBook()
    
    if request.method=='POST':
        book_form=NewBook(request.POST,files=request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect('home')
        else:
            print('Not valid')
    context={
        'form':book_form,
    }   
    return render(request,'boitoi/add_book.html',context)
    
    # Edit Book 

def EditBookDetails(request,pk):
    book=Book.objects.get(id=pk)
    book_form=NewBook(instance=book)
    if request.method=='POST':
        book_form=NewBook(request.POST,files=request.FILES,instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('home')
        else:
            print('Not valid')
    context={
        'form':book_form,
    }
    return render(request,'boitoi/edit_book.html',context)

def DeleteBook(request,pk):
    book=Book.objects.get(id=pk)
    context={
        'book':book,
    }
    if request.method=='POST':
        book.delete()
        return redirect('home')
    return render(request,'boitoi/delete_book.html',context)


def EditOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=EditOrderForm(instance=order)
    if  request.method=='POST':
        form =EditOrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    context={
        'order':order,
        'form':form,
    }
    return render(request,'boitoi/edit_order.html',context)


def Search(request):
    booklist=[]
    context={}
    if request.method=='POST':
        txt=request.POST.get('search_box_text')
        booklist+=Book.objects.filter(
            name__unaccent__lower__trigram_similar=txt
            )
        
        for i in Author.objects.filter(name__unaccent__icontains=txt):
            booklist+=i.book_set.all()
        


        booklist=set(booklist)
        booklist=list(booklist)
        print(booklist)
        context={
            'books':booklist,
            'txt':txt
        }

    return render(request,'boitoi/search_nald.html',context)




def AddItems(request):
    return render(request,'boitoi/add_items.html')