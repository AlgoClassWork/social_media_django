from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Post

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()
    return render(request, 'register.html', {'form' : form} )

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})
