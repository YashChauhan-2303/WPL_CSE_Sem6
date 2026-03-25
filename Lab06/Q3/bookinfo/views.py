from django.shortcuts import render


def home(request):
    book = {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'cover_image': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400&h=600&fit=crop',
    }
    return render(request, 'bookinfo/home.html', {'book': book})


def metadata(request):
    book = {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'isbn': '978-0-7432-7356-5',
        'language': 'English',
        'pages': 180,
        'genre': 'Novel, Fiction, Tragedy',
        'published_date': 'April 10, 1925',
        'format': 'Hardcover, Paperback, eBook',
    }
    return render(request, 'bookinfo/metadata.html', {'book': book})


def reviews(request):
    book = {
        'title': 'The Great Gatsby',
    }
    reviews_list = [
        {
            'reviewer': 'The New York Times',
            'rating': 5,
            'comment': 'A masterpiece of American literature that captures the essence of the Jazz Age.',
        },
        {
            'reviewer': 'Literary Digest',
            'rating': 4,
            'comment': 'Fitzgerald\'s prose is elegant and evocative, painting vivid pictures of 1920s New York.',
        },
        {
            'reviewer': 'Book Review Magazine',
            'rating': 5,
            'comment': 'An enduring classic that explores themes of wealth, love, and the American Dream.',
        },
    ]
    return render(request, 'bookinfo/reviews.html', {'book': book, 'reviews': reviews_list})


def publisher(request):
    publisher_info = {
        'name': 'Charles Scribner\'s Sons',
        'address': '597 Fifth Avenue, New York, NY 10017',
        'phone': '+1 (212) 555-0123',
        'email': 'contact@scribners.com',
        'website': 'www.scribners.com',
        'founded': '1846',
        'description': 'Charles Scribner\'s Sons is an American publisher based in New York City, known for publishing works by Ernest Hemingway, F. Scott Fitzgerald, and many other notable authors.',
    }
    book = {
        'title': 'The Great Gatsby',
    }
    return render(request, 'bookinfo/publisher.html', {'publisher': publisher_info, 'book': book})
