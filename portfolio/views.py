from django.shortcuts import render
from portfolio.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })