from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, Phone: {phone}, Message: {message}')
        return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
