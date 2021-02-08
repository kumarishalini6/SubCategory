from django.shortcuts import render
from .models.category import Category


def index(request):
    category = Category.objects.all()
    return render(request, 'indedx.html', {'category':category})