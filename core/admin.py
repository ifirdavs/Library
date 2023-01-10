from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('student_id','name')
    list_display = ('id','student_id','name','gender','grade',)
    list_display_links = ('student_id','name','gender','grade')
    list_filter = ('gender','grade',)
    ordering = ('id',)
    list_per_page = 12
    # fields = ()

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'birth_year')
    list_display = ('id', 'name', 'birth_year', 'alive')
    list_display_links = ('id', 'name')
    list_editable = ('alive',)                                     # DON'T forget comma after single-item tuples!!!
    list_filter = ('alive',)
    ordering = ('id',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'author__name')
    list_display = ('id', 'name', 'publication_date', 'get_authors')    # 
    list_display_links = ('id', 'name', 'publication_date')
    list_filter = ('author',)
    ordering = ('id',)
    autocomplete_fields = ('author',)                                   

    def get_authors(self, obj):                                         # "obj" is our model object
        return obj.get_authors()                                        # to show all authors in a table
    
    get_authors.short_description = 'authors'                           # column name = 'authors' in a table

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    search_fields = ('student__name', 'book__name')
    list_display = ('id', 'student', 'get_books', 'took_date', 'returned')
    list_display_links = ('id', 'student', 'get_books')
    list_filter = ('returned',)
    ordering = ('id',)
    autocomplete_fields = ('student','books')                           # when adding a record among 2000 students
    
    def get_books(self, obj):                                           # "obj" is our model object
        return obj.get_books()                                          # to show all books in a table
    
    get_books.short_description = 'books'                               # column name = 'books' in a table
