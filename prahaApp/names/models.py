from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length=10)
    nickName = models.CharField(max_length=20)
    surName = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    def __str__(self):
        return self.firstName
