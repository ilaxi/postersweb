
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    short_bio = models.CharField(max_length=60, blank=True)
    avatar = models.URLField(blank=True, default="https://api.dicebear.com/7.x/avataaars/svg")
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    preview_title = models.CharField(max_length=255, blank=True, null=True)
    preview_image = models.URLField(blank=True, null=True)
    preview_url = models.URLField(blank=True, null=True)
    preview_domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def get_likes_count(self):
        return self.likes.count()

    def get_comments_count(self):
        return self.comments.all().count()
        
    def get_relative_time(self):
        from django.utils import timezone
        now = timezone.now()
        diff = now - self.created_at
        
        minutes = int(diff.total_seconds() / 60)
        if minutes < 60:
            return f'hace {minutes} m'
        
        hours = int(minutes / 60)
        if hours < 24:
            return f'hace {hours} h'
        days = int(hours / 24)
        return f'hace {days} d'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='comments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    preview_title = models.CharField(max_length=255, blank=True, null=True)
    preview_image = models.URLField(blank=True, null=True)
    preview_url = models.URLField(blank=True, null=True)
    preview_domain = models.CharField(max_length=255, blank=True, null=True)

    def get_relative_time(self):
        from django.utils import timezone
        now = timezone.now()
        diff = now - self.created_at
        
        minutes = int(diff.total_seconds() / 60)
        if minutes < 60:
            return f'hace {minutes} m'
            
        hours = int(minutes / 60)
        if hours < 24:
            return f'hace {hours} h'
        
        days = int(hours / 24)
        return f'hace {days} d'


    class Meta:
        ordering = ['created_at']

    def get_likes_count(self):
        return self.likes.count()
