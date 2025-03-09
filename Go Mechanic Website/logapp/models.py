from django.db import models

# Create your models here.

class Contact (models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

    class Meta:
        db_table = "contact"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "customer"


class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)
    address = models.TextField()
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "mechanic"


class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "admin"


class Book(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    slot_status = models.CharField(max_length=150, default='pending')

    class Meta:
        db_table = "book"


class Review(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.BigIntegerField()
    review = models.CharField(max_length=100)

    class Meta:
        db_table = "review"



