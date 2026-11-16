from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Post


# Create your views here.

def home_view(request: HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by("-published_at")
    return render(request, "main/home.html", {"posts": posts})


def add_post_view(request: HttpRequest):
    if request.method == "POST":
        post = Post(
            title=request.POST["title"],
            author=request.POST["author"],
            content=request.POST["content"],
            is_published="is_published" in request.POST,
        )
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:home_view")

    return render(request, "main/add_post.html")

def post_detail_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "main/post_detail.html", {"post": post})

def update_post_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.author = request.POST["author"]
        post.content = request.POST["content"]
        post.is_published = "is_published" in request.POST
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()
        return redirect("main:post_detail_view", post_id=post.id)

    return render(request, "main/update_post.html", {"post": post})

def delete_post_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()

    return redirect("main:home_view")