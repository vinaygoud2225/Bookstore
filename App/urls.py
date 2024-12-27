from django.urls import path
from . import views

urlpatterns = [
    path('',views.BookListview.as_view(),name='book_list'),
    path('book/<int:pk>/',views.BookDetailview.as_view(),name='book_detail'),
    path('book/<int:pk>/edit/',views.BookUpdateview.as_view(),name='book_edit'),
    path('book/<int:pk>/delete/', views.BookDeleteview.as_view(), name='book_delete'),
    path('book/add/',views.BookCreateview.as_view(),name='book_add'),

]





