from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post , Repost
from .forms import PostForm, PostUpdateForm ,CommentForm
from django.contrib.auth.decorators import login_required



# this is the homepage
@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})




# make post
def make_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:index')  # Redirect to the newly created post
    else:
        form = PostForm()
       
    return render(request, 'blog/makepost.html', {'form': form})


# post_details page
def post_details(request, pk):
    post = Post.objects.get(id=pk)
    if request.method =='POST':
      c_form = CommentForm(request.POST)
      if c_form.is_valid():
        instance  =  c_form.save(commit=False)
        instance.user = request.user
        instance.post = post
        instance.save()
        return redirect('blog:post_details', pk=post.id)
    else:
        c_form = CommentForm()
    context={
          'post':post,
          'c_form':c_form,
    }


    return render(request,'blog/post_details.html', context)


# post_edit page
def post_edit(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_details',pk=post.id)
    else:
         form = PostUpdateForm(instance=post)
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request,'blog/edit_post.html',context)




# delete post


def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index',)
    return render(request,'blog/post_delete.html', {'post':post})



# repost view
@login_required
def toggle_repost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    has_reposted = Repost.objects.filter(user=request.user, post=post).exists()

    context = {
        'post': post,
        'has_reposted': has_reposted,
    }
    return render(request, 'post_detail.html', context)

  
