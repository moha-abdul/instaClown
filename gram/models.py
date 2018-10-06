from django.db import models

class Profile(models.Model):
    profile_bio = models.CharField(max_length=50)
    profile_photo  = models.ImageField(upload_to = 'profile/')

class Image(models.Model):
    image_image  = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile)
    

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

    def __str__(self):
        return self.post_caption()
