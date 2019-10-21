from django.db import models
from datetime import *



class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['titleName']) < 2:
            errors["titleName"] = "Title name should be at least 2 characters"
        if len(postData['networkName']) < 3:
            errors["networkName"] = "Network name should be at least 3 characters"
        if len(postData['descriptionName']) < 10 and len(postData['descriptionName']) > 0:
            errors["descriptionName"] = " Description should either be blank or at least 10 characters"
        if datetime.strptime(postData['dateName'], "%Y-%m-%d") < datetime.today():
            errors["dateName"] = " release date should be in the past"
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()  



    # fields removed for brevity
    def __repr__(self):
        return f"<Shows object: {self.title} ({self.id})>"

    # Shows.objects.create(title ="Stranger Things", network = "Netflix", description = "a show about a girl with powers and the 1980's", release_date = "2017-06-01")