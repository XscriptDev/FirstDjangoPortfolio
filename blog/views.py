from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
# Create your views here.
def blog(request):
    blogs = Blog.objects.order_by("-date")
    return render(request , "blog/home.html",{'blogs':blogs})
def spblog(request,blog_id):
    theblog = get_object_or_404(Blog , pk=blog_id)
    return render(request , "blog/dblog.html" , {"blog":theblog})
