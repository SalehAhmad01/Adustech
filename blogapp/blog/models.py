from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comments_set.all().count()

    def repost_count(self):
        return self.repost_set.count()

    def time_since_posted(self):
        now = timezone.now()
        date_created = timezone.localtime(self.date_created)
        time_difference = now - date_created

        if time_difference < timedelta(days=2):
            if time_difference < timedelta(minutes=1):
                return "just now"
            elif time_difference < timedelta(hours=1):
                minutes = int(time_difference.total_seconds() // 60)
                return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
            elif time_difference < timedelta(days=1):
                hours = int(time_difference.total_seconds() // 3600)
                return f"{hours} hour{'s' if hours > 1 else ''} ago"
            else:
                days = time_difference.days
                return f"{days} day{'s' if days > 1 else ''} ago"

        return date_created.strftime("%B %d, %Y, %I:%M %p")

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content

class Repost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_reposted = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Prevent duplicate reposts

    def __str__(self):
        return f"{self.user.username} reposted {self.post.title}"
