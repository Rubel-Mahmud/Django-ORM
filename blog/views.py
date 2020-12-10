from django.shortcuts import render
from .models import Blog

def index(request):
    context = Blog.objects.all().order_by('-id')
    return render(request, 'blog/index.html', {
        'context':context
    })
