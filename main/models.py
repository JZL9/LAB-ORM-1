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


class Review(models.Model):

    class Rating(models.IntegerChoices):
        POOR = 1, "⭐ Poor"
        FAIR = 2, "⭐⭐ Fair"
        GOOD = 3, "⭐⭐⭐ Good"
        VERY_GOOD = 4, "⭐⭐⭐⭐ Very Good"
        EXCELLENT = 5, "⭐⭐⭐⭐⭐ Excellent"

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    reviewer_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=Rating.choices, default=Rating.EXCELLENT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.post.title}"