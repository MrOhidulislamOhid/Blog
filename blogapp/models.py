from xml.etree.ElementTree import Comment

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='category_creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):

    STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comments(models.Model):

    COMMENT_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ]



    user_comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    status = models.CharField(max_length=10, choices=COMMENT_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
    



class UserPermission(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee_user_for_permission") 
    post          = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_for_permission") 
    can_view      = models.BooleanField(default=False)
    can_add       = models.BooleanField(default=False)
    can_update    = models.BooleanField(default=False)
    can_delete    = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created_by    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by_user") 
    updated_by    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by_user", blank=True, null=True) 
    deleted_by    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deleted_by_user", blank=True, null=True)
    is_active     = models.BooleanField(default=True)
    deleted       = models.BooleanField(default=False)

    class Meta:
        db_table = "user_permission"
        

    def __str__(self):
        return str(self.post) 