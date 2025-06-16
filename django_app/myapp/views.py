from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Book
import json

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

# GET all books
def api_all_books(request):
    books = Book.objects.all()
    books_list = [
        {"id": b.id, "title": b.title, "author": b.author, "year_published": b.year_published}
        for b in books
    ]
    return JsonResponse(books_list, safe=False, content_type="application/json")

# GET single book by query param: ?id=1
def api_single_book(request):
    book_id = request.GET.get("id")
    try:
        book = Book.objects.get(id=book_id)
        data = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year_published": book.year_published,
        }
        return JsonResponse(data, content_type="application/json")
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, content_type="application/json")

# POST new book data
@csrf_exempt
@require_http_methods(["POST"])
def api_create_book(request):
    try:
        body = json.loads(request.body)
        title = body.get("title")
        author = body.get("author")
        year = body.get("year_published")

        if not all([title, author, year]):
            raise ValueError("Missing fields")

        new_book = Book.objects.create(title=title, author=author, year_published=year)
        return JsonResponse(
            {"success": f"Book '{new_book.title}' added."},
            status=200,
            content_type="application/json"
        )
    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=200,
            content_type="application/json"
        )