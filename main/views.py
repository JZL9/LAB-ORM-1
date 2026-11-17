from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Post


# Create your views here.

def home_view(request: HttpRequest):
    posts = (
        Post.objects.filter(is_published=True)
        .exclude(image="")
        .order_by("-published_at")[:7]
    )

    #posts = Post.objects.all()[0:5]
    
    return render(request, "main/home.html", {"posts": posts})


def add_post_view(request: HttpRequest):
    if request.method == "POST":
        category = request.POST.get("category", Post.Category.OTHER)
        if category not in Post.Category.values:
            category = Post.Category.OTHER

        post = Post(
            title=request.POST["title"],
            author=request.POST["author"],
            category=category,
            content=request.POST["content"],
            is_published="is_published" in request.POST,
        )
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:home_view")

    return render(request, "main/add_post.html", {"categories": Post.Category.choices})

def post_detail_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "main/post_detail.html", {"post": post})

def update_post_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        category = request.POST.get("category", post.category)
        if category in Post.Category.values:
            post.category = category

        post.title = request.POST["title"]
        post.author = request.POST["author"]
        post.content = request.POST["content"]
        post.is_published = "is_published" in request.POST
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:post_detail_view", post_id=post.id)

    return render(request, "main/update_post.html", {"post": post, "categories": Post.Category.choices})

def delete_post_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()

    return redirect("main:home_view")

def all_posts_view(request: HttpRequest):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")

    posts = Post.objects.filter(is_published=True)
    if query:
        posts = posts.filter(title__icontains=query)
    if category in Post.Category.values:
        posts = posts.filter(category=category)
    posts = posts.order_by("-published_at")

    total = posts.count()
    return render(request, "main/all_posts.html", {
        "posts": posts,
        "total": total,
        "query": query,
        "category": category,
        "categories": Post.Category.choices,
    })