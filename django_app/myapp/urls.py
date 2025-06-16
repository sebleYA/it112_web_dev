from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
     # API Routes
    path('api/books/', views.api_all_books),
    path('api/book/', views.api_single_book),
    path('api/book/', views.api_create_book),  # Same path as above, but for POST
]