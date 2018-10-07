from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    profile_bio = models.CharField(max_length=50)
    profile_photo  = models.ImageField(upload_to = 'profile/')

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name='user')
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

class Image(models.Model):
    image_image  = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=50, null=True)
    image_caption = models.CharField(max_length=50, default="")
    profile = models.ForeignKey(Profile)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    # likes = models.IntegerField(default=0)
    

    def save_image(self):
        '''
        method to save image
        '''
        self.save()

    def delete_image(self):
        '''
        method to delete image
        '''
        self.delete()

    # def update_caption():
    #     self.update()

    # def __str__(self):
    #     return self.post_caption()
