from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
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


def Delete(request, id):
    try:
        blog = Blog.objects.get(pk=id)
        blog.delete()
    except blog.DoesnotExist:
        return HttpResponse('blog object doesnot exist.')

    return HttpResponseRedirect('/')