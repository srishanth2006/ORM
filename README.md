# Ex02 Django ORM Web Application
## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagra
![er](https://github.com/srishanth2006/ORM/assets/150319470/f5d47271-cdeb-44a6-adb1-5816b5286e77)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
model.py
from django.db import models 
from django.contrib import admin
class Book_DB(models.Model):
    Bookno=models.IntegerField(primary_key="Bookno");
    Bookname=models.CharField(max_length=20);
    author=models. EmailField();
    pageno=models.DateField();
    language=models.IntegerField();
class Book_DBAdmin(admin.ModelAdmin):
    list_display=("Bookno", "Bookname", "author", "pageno","language");

Admin.py
from django.contrib import admin
from.models import Book_DB,Book_DBAdmin
admin.site.register(Book_DB,Book_DBAdmin)
```
## OUTPUT
![alt text](<Screenshot 2024-02-28 093934.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
