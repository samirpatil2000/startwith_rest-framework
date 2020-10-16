from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from account.models import Account
from .forms import CreateBlogPostForm,UpdateBlogPostForm
# Create your views here.
def blog_index(request):
    blog=BlogPost.objects.all()
    context={
        'blog':blog,
    }
    return render(request,'blog/home.html',context)

def create_blog(request):

    if not request.user.is_authenticated:
        return redirect('login')
    form=CreateBlogPostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        obj=form.save(commit=False)  #TODO commit=False we have to save one more IMPORTANT field that is "" author ""
        email=Account.objects.filter(email=request.user.email)[0]
        obj.author=email
        obj.save()
        return redirect('blog_index')
    context={
        'form':form
    }

    return render(request,'blog/create.html',context )

def detail_blog_view(request, slug):

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context={
        'blog_post' : blog_post
    }
    return render(request, 'blog/detail_blog.html', context)

def update_blog_post(request,slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    author=blog_post.author
    if not request.user.is_authenticated:
        redirect('login')
    if request.user != author:
        return HttpResponse("You can't edit this post ")

    if request.POST:
        updateForm=UpdateBlogPostForm(request.POST or None,request.FILES or None,instance=blog_post)
        if updateForm.is_valid():
            obj=updateForm.save(commit=False)
            obj.save()
            blog_post=obj

    form=UpdateBlogPostForm(
        initial={
            "title":blog_post.title,
            "body":blog_post.body,
            "image": blog_post.image,
        }
    )
    context={
        'form':form
    }
    return render(request, 'blog/edit_blog.html', context)

