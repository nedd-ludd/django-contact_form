from django.db import models

class Mail_requestee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254 )
    message = models.TextField()

    def __str__(self):
        return f'{self.firstName} {self.lastName}'