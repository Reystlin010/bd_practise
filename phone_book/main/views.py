from django.shortcuts import render
from .models import Users


def index(request):
    return render(request, 'main/index.html')

def new_record(request):
    return render(request, 'main/records.html')

def show_tables(request):
    all_data = Users.objects.all()
    return render(request, 'main/show_tables.html', {"data": all_data})

def create(request):
    return render(request, 'main/create.html')