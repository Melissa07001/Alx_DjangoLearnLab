from django.db import models

<<<<<<< HEAD
class Author(models.Model):
    # The name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)
    # Year the book was published
    publication_year = models.IntegerField()
    # Link to the author (one author can have many books)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
=======
# Create your models here.
>>>>>>> c44adeb1cd238ee62f92fa0072aa93fd5902541e
