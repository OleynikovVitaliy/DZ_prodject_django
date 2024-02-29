import csv
import os
from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(request, 'main/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('data.csv', 'a', newline='') as file:
            fieldnames = ['Date', 'Name', 'Phone', 'Massage']
            data = csv.DictWriter(file, fieldnames=fieldnames)
            file_empty = os.stat('data.csv').st_size == 0
            if file_empty:
                data.writeheader()
            data.writerow({'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Name': name, 'Phone': phone,
                           'Message': message})

    return render(request, 'main/contacts.html')
