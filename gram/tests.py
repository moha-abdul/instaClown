from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile, Comment

class UserTest(TestCase):
    def setUp(self):
        self.user = User(username = 'moha', first_name = 'Moha', last_name = 'Med', email='max@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_data(self):
        self.assertTrue(self.user.username, "moha")
        self.assertTrue(self.user.first_name, "Moha")
        self.assertTrue(self.user.last_name, 'Med')
        self.assertTrue(self.user.email, 'max@gmail.com')

    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users) == 0)

class ProfileTest(TestCase):
    def setUp(self):
        self.new_user = User(username = 'moha', first_name = 'Moha', last_name = 'Med', email = 'max@gmail.com')
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user, profile_bio='my bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_data(self):
        self.assertTrue(self.new_profile.profile_bio, "my bio")
        self.assertTrue(self.new_profile.user, self.new_user)

    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete(self):
        profile = Profile.objects.filter(id=1)
        profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(profile_bio = 'my bio').update(profile_bio = 'welcome')
        self.updated_profile = Profile.objects.get(profile_bio = 'welcome')
        self.assertTrue(self.updated_profile.profile_bio, 'welcome')