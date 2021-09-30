from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from restaurant.models import *

# Create your views here.

def review(request):
    reviews = Comment.objects.all()
    category = Category.objects.all()
    user = request.user
    return render(request, "review.html",{'reviews':reviews, 'user':user, 'category':category})

def filter(request, id): 
    reviews = Comment.objects.filter(restaurant__category__id__contains = id)
    category = Category.objects.all()
    user = request.user
    return render(request, "filter.html",{'reviews':reviews, 'user':user, 'category':category})
