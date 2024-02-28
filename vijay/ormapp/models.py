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
