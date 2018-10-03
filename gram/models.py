from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=50)
    username  = models.CharField(max_length=50)

    def __str__(self):
            return self.username()
