from django.db import models


class Hogwarts(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

# # SQL TO ORM
# # INSERT INTO Hogwarts (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');copy
# Hogwarts.objects.create(name = 'Harry Potter', house = 'Gryffindor', pet = 'hedwig', year = '5')

# # INSERT INTO Hogwarts (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');
# Hogwarts.objects.create(name = 'Hermione Granger', house = 'Gryffindor', pet = 'Crookshanks', year = '5')

# # SELECT * FROM Hogwarts WHERE id = 1;
# Hogwarts.objects.filter(id = '1')

# # SELECT * FROM Hogwarts WHERE house = 'Gryffindor';
# Hogwarts.objects.filter(house = 'Gryffindor')

# # UPDATE Hogwarts SET year = '6' WHERE id = 1;
# c = Hogwarts.objects.get(id = '1')
# c.year = 6
# # c.save()


# # # ORM TO SQL

# # # Hogwarts.objects.create(name="Draco Malfoy", house="Slytherin", pet="Unknown", year="5")
# # INSERT INTO Hogwarts (name, house, pet, year) VALUES ('Draco Malfoy', 'Slytherin', 'Unknown', '5');

# # # Hogwarts.objects.create(name="Luna Lovegood", house="Ravenclaw", pet="None", year="4")
# # INSERT INTO Hogwarts (name, house, pet, year) VALUES ('Luna Lovegood', 'Ravenclaw', 'None', '4');

# # # Hogwarts.objects.create(name="Padma Patil", house="Ravenclaw", pet="None", year="5")
# # INSERT INTO Hogwarts (name, house, pet, year) VALUES ('Padma Patil', 'Ravenclaw', 'None', '5');

# # # ravenclaws = Hogwarts.objects.filter(house="Ravenclaw")
# # SELECT * FROM Hogwarts WHERE  house =avenclaw';

# # # luna = Hogwarts.objects.get(name="Luna Lovegood")
# # # luna.year = 5
# # # luna.save()

# # UPDATE Hogwarts SET year = '5' WHERE name = 'Luna Lovegood';

class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# #  Query: Create 3 new users
# users.objects.create(first_name="Draco Malfoy", last_name="Slytherin", email_address="Unknown", age="25")
# users.objects.create(first_name="Harry Potter", last_name="Gryffindor", email_address="Hedwig", age="25")
# users.objects.create(first_name="Hermione Granger", last_name="Gryffindor", email_address="Crookshank", age="25")

# #  Query: Retrieve all the users
# users.objects.all()

# #  Query: Retrieve the last user
# users.objects.last()

# #  Query: Retrieve the first user
# users.objects.first()

# #  Query: Change the user with id=3 so their last name is Pancakes.
# c = users.objects.get(id=3)
# c.last_name = "Pancakes"
# c.save()

# #  Query: Delete the user with id=2 from the database
# c = users.objects.get(id=2)
# c.delete()

# #  Query: Get all the users, sorted by their first name
# users.objects.all().order_by("first_name")
# #  BONUS Query: Get all the users, sorted by their first name in descending order
# users.objects.all().order_by("-first_name")
# #  Submit your .txt file that contains all the queries you ran in the shell



# Dojo Class and Ninja

class dojo(models.Model):
    first_name = models.CharField(max_length=255)
    city =  models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(max_length=600)

class ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    assigned_dojo = models.ForeignKey(dojo, related_name="enrolled_ninjas")
# the thing that is foriegn iss the table DOJO, the foreign key goes on the many  filter(first_name = "OC DOJO")

# # # #  Query: Create 3 new users
# dojo.objects.create(first_name="LA DOJO", city="LA", state = "CA")
# dojo.objects.create(first_name="SF DOJO", city="SF", state = "CA")
# dojo.objects.create(first_name="OC DOJO", city="OC", state = "CA")

# ninja.objects.create(first_name="Harry", last_name="Potter", assigned_dojo= dojo.objects.get(id = "1"))

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

# books.create(title ="java", desc = "a book java")
# books.create(title ="C-Sharp", desc = "a book CSHARP")
# books.create(title ="Pyhton", desc = "a book Python")
# books.create(title ="PHP", desc = "a book PHP")
# books.create(title ="Ruby", desc = "a book Ruby")

# authors.create(first_name="Jane", last_name="Austen")
# authors.create(first_name="Emily", last_name="Dickson")
# authors.create(first_name="Fyodor", last_name="Dostevksy")
# authors.create(first_name="William", last_name="Shakespeare")
# authors.create(first_name="Lau", last_name="Tzu")


