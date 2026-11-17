from django.db import models

# Create your models here.



class Post(models.Model):

    class Category(models.TextChoices):
        TECH = "tech", "Technology"
        PROGRAMMING = "programming", "Programming"
        DESIGN = "design", "Design"
        AI = "ai", "AI"
        OTHER = "other", "Other"

    title = models.CharField(max_length=2048)
    author = models.CharField(max_length=100, default="Anonymous")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title
