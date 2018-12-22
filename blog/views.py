from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def index(request):
    return render(request, 'blog/index.html')

def form(request):
    return render(request, 'blog/form.html')

def maps(request):
    return render(request, 'blog/maps.html')

def news(request):
    return render(request, 'blog/news.html')

def why(request):
    return render(request, 'blog/why.html')
