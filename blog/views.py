from django.shortcuts import render
from .models import Blog

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tagline = request.POST.get('tagline')
        Blog.objects.create(name=name, tagline=tagline)
    context = Blog.objects.all()
    return render(request, 'blog/index.html', {
        'context':context,
    })

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        tagline = request.POST.get('tagline')
        blog = Blog.objects.get(pk=id)
        blog.name = name
        blog.tagline = tagline
        blog.save()
        return redirect('/')
    else:
        blog = Blog.objects.get(pk=id)
        name = blog.name
    context = {
        'name':name,
        'tagline':tagline
    }
    return render(request, 'blog/index.html', {
        'context':name
    })