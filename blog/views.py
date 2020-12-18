from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Blog, Comments
from blog.forms import BlogAddForm


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


def addBlog(request):
    if request.method == 'POST':
        form = BlogAddForm(request.POST)
    else:
        form = BlogAddForm()
    return render(request, 'blog/add.html', {
        'form':form
    })


def delete(request, id):
    try:
        blog = Blog.objects.get(pk=id)
        blog.delete()
    except blog.DoesnotExist:
        return HttpResponse('blog object doesnot exist.')

    return HttpResponseRedirect('/')

#@login_required
def item_detail(request, id):
    context = Blog.objects.all().order_by('-id')
    item = Blog.objects.get(pk=id)
    comments = Comments.objects.all().filter(blog=item).order_by('-id')
    #username = comments.author.username
    #nameFirstCharacter = username[0]
    return render(request, 'blog/item_detail.html', {
        'item':item, 'context':context, 'comments':comments
    })

@login_required
def comments(request, id):
    if request.user.is_authenticated:
        currentUser_id = request.user.id
        currentUser = User.objects.get(pk=currentUser_id)
        message = ''
        context = Blog.objects.all().order_by('-id')
        item = Blog.objects.get(pk=id)
        if request.method == 'POST':
            comment = request.POST.get('comment')
            if comment != '' and comment != None:
                addComment = Comments(blog=item, author=currentUser, caption=comment)
                addComment.save()
                return HttpResponseRedirect('/blog/item/' + str(id))
            else:
                message = "You didn't type anything."
    else:
        currentUser = None
    return render(request, 'blog/comments.html', {
        'context':context, 'item':item, 'message':message, 'currentUser':currentUser
    })
