from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Author, Publisher, Book
from .forms import AuthorForm, PublisherForm, BookForm


def index(request):
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'publishers': publishers,
        'books': books,
    }
    return render(request, 'index.html', context)


# Author Views
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})


@require_http_methods(["GET", "POST"])
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form, 'title': 'Create Author'})


@require_http_methods(["GET", "POST"])
def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form, 'title': 'Edit Author'})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'confirm_delete.html', {'object': author, 'type': 'Author'})


# Publisher Views
def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})


def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    books = publisher.book_set.all()
    return render(request, 'publisher_detail.html', {'publisher': publisher, 'books': books})


@require_http_methods(["GET", "POST"])
def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'publisher_form.html', {'form': form, 'title': 'Create Publisher'})


@require_http_methods(["GET", "POST"])
def publisher_edit(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_detail', pk=publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'publisher_form.html', {'form': form, 'title': 'Edit Publisher'})


def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'confirm_delete.html', {'object': publisher, 'type': 'Publisher'})


# Book Views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


@require_http_methods(["GET", "POST"])
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form, 'title': 'Create Book'})


@require_http_methods(["GET", "POST"])
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'title': 'Edit Book'})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'object': book, 'type': 'Book'})
