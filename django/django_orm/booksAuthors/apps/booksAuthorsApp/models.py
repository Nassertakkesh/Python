from django.db import models

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)


    def __repr__(self):
        return f"<book object: {self.title} ({self.id})>"

class author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books =  models.ManyToManyField(book, related_name="booking")
    notes = models.CharField(max_length=255,default= 'notes') 

    def __repr__(self):
        return f"<Author object: {self.first_name} {self.last_name} {self.books}  ({self.id})>"