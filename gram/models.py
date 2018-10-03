from django.db import models

class Uzer(models.Model):
    full_name = models.CharField(max_length=50)
    username  = models.CharField(max_length=50)

    def save_user(self):
        '''
        method to save user
        '''
        self.save()

    def delete_user(self):
        '''
        method to delete user
        '''
        self.delete()

    def __str__(self):
        return self.username()
