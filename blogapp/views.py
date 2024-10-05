from django.shortcuts import render, get_object_or_404
from blogapp.models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,"blogapp/index.html",{'allposts': posts})

def single_page(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/single_post.html', {'post': post})