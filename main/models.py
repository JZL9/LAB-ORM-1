from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=2048)
    author = models.CharField(max_length=100, default="Anonymous")
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title
