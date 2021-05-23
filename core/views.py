# core/views.py
from django.shortcuts import render
from django.contrib.auth.models import User              
from django.core.paginator import Paginator, EmptyPage


def list_users(request, page=1):
    users = User.objects.all()
    paginator = Paginator(users, 5) # 5 users per page
    
    # We don't need to handle the case where the `page` parameter
    # is not an integer because our URL only accepts integers
    try:
        users = paginator.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page 
        users = paginator.page(paginator.num_pages)
            
    return render(request, 'home.html', {'users': users})