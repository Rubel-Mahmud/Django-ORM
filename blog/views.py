from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Blog, Comment


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


def delete(request, id):
    try:
        blog = Blog.objects.get(pk=id)
        blog.delete()
    except blog.DoesnotExist:
        return HttpResponse('blog object doesnot exist.')

    return HttpResponseRedirect('/')


def item_detail(request, id):
    context = Blog.objects.all().order_by('-id')
    item = Blog.objects.get(pk=id)
    return render(request, 'blog/item_detail.html', {
        'item':item, 'context':context
    })


def comments(request, id):
    message = ''
    context = Blog.objects.all().order_by('-id')
    item = Blog.objects.get(pk=id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment != '' and comment != None:
            addComment = Comment(blog=item, caption=comment)
            addComment.save()
            return HttpResponseRedirect('/blog/item/' + str(id))
        else:
            message = "You didn't type anything."

    return render(request, 'blog/comments.html', {
        'context':context, 'item':item, 'message':message
    })