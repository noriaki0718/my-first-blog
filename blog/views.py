from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

def post_list(request):
    return render(request, 'blog/post_list.html',{})
    user = User.objects.get(username='your_username')
    post = Post(author=user, title='Sample title', text='Test content', created_date=timezone.now())
    post.save()
# Create your views here.
