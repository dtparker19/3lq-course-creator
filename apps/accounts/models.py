from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from core import settings
#from accounts.admin import CustomUserAdmin
# Create your models here.
# create a class for the custom user model


class CustomUser(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    #USERNAME_FIELD = 'email'
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    #CustomUserAdmin = CustomUserAdmin(User, fields=('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'username'), extra=3)
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile
    
    @classmethod
    def get_profile_by_id(cls, id):
        profile = Profile.objects.get(id=id)
        return profile
    
    @classmethod
    def update_profile(cls, id, bio):
        profile = Profile.objects.get(id=id)
        profile.bio = bio
        profile.save()
        return profile
    
    @classmethod
    def update_profile_pic(cls, id, profile_pic):
        profile = Profile.objects.get(id=id)
        profile.profile_pic = profile_pic
        profile.save()
        return profile
