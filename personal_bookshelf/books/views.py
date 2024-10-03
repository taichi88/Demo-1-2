from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm
# Create your views here.


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    
    return render(request, 'books/book_edit.html', {'form': form})


def book_detail(request, pk):
    #amisatvis unda davaimporto get_objevt, rac nishanvs rom an momiva obieqti an daabrune 404 error
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)

    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'form': form})

def author_edit(request, pk):
    author = get_object_or_404(author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_detail', pk=author.pk)

    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/author_edit.html', {'form': form})

def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()

    return render(request, 'authors/author_edit.html', {'form':form})



def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})





