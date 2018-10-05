from django.db import models

class Posts(models.Model):
    post_caption = models.CharField(max_length=50)
    post_image  = models.ImageField(upload_to = 'images/')

    def save_posts(self):
        '''
        method to save posts
        '''
        self.save()

    def delete_posts(self):
        '''
        method to delete posts
        '''
        self.delete()

    def __str__(self):
        return self.post_caption()
