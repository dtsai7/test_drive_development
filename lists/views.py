from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html', {'new item list': request.POST.get('item_text', ''),
    })
