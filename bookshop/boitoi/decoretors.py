from django.shortcuts import render,redirect


def authenticated_user(view_func):
    def container(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    return container