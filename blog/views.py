from django.shortcuts import render
from .models import Blog


def index(request):
    message = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        tagline = request.POST.get('tagline')
        if name != '' and name != None and tagline != '' and tagline != None:
            blog = Blog(name=name, tagline=tagline)
            blog.save()
            message = 'Add blog ' + str(blog.id) + 'succesfully.'
        else:
            message = 'Add blog failed.'
    context = Blog.objects.all().order_by('-id')
    return render(request, 'blog/index.html', {
        'message':message, 'context':context
    })
