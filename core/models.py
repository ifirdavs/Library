from django.db import models


class Student(models.Model):
    G = (
        ("freshman","Freshman"),
        ("sophomore","Sophomore"),
        ("junior", "Junior"),
        ('senior', 'Senior')
    )
    student_id = models.PositiveIntegerField()
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25, choices=(("male","Male"), ("female","Female")))
    grade = models.CharField(max_length=25, choices=G, null=True)
    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=40)
    about = models.TextField(blank=True, null=True)
    birth_year = models.PositiveIntegerField(null=True,blank=True)
    alive = models.BooleanField(default=1)
    picture = models.FileField(null=True)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    publication_date = models.DateField(null=True)
    author = models.ManyToManyField(Author, verbose_name='Authors', related_name='books')                   # MtM
    description = models.TextField(default="")
    cover_image = models.FileField(null=True)

    def get_authors(self):
        return ", ".join([str(x) for x in self.author.all()])

    def __str__(self) -> str:                                                       # when __unicode__: in Django Admin Panel it shows Author object (1)
        return self.name

class Record(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)                   # FK
    books = models.ManyToManyField(Book)                                            # MtM
    took_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField(default=False)
    
    def get_books(self):
        return "; ".join([str(x) for x in self.books.all()])

    def __str__(self) -> str:
        return f"{self.student.name}"
    

