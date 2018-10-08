from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_bio = models.TextField(max_length=50)
    profile_photo  = models.ImageField(upload_to = 'profile/')

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        instance.profile.save()
        
    

class Comment(models.Model):
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name='user')
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

class Image(models.Model):
    image_image  = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=50, null=True)
    image_caption = models.CharField(max_length=50, default="")
    profile = models.ForeignKey(Profile, null=True)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    

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
