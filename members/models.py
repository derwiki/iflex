from django.db import models

# Wrapper class for django auth
class Member (models.Model): # Actually 'User,' but since User is used by Django's authentication system, we use 'Member,' as though in a fitness club

    firstName = models.CharField(max_length=64)

    lastName = models.CharField(max_length=64)
    
    password = models.CharField(max_length=64)

    age = models.IntegerField()

    height = models.IntegerField() # in inches
    
    weight = models.IntegerField() # In pounds

    def __str__(self):
        return (str(self.id) + ', ' + self.firstName + ', ' + self.lastName + ', ' + str(self.age) + ', ' + str(self.height) + ', ' + str(self.weight))
