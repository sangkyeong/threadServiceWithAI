from books.models import Book
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_books_from_fixture(target_book, num=3):
    all_books = Book.objects.exclude(pk=target_book.pk)

    descriptions = [target_book.description] + [book.description for book in all_books]
    books_list = list(all_books)

    vectorizer = TfidfVectorizer().fit_transform(descriptions)
    similarities = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()

    similar_books = sorted(zip(similarities, books_list), key=lambda x: x[0], reverse=True)

    return [book for _, book in similar_books[:num]]