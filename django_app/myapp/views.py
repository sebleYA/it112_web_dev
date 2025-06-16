from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
from django.shortcuts import render

def home_view(request):
    user_name = request.GET.get('user_name', None)
    return render(request, 'base.html', {'user_name': user_name})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
