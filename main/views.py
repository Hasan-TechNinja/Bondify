from django.shortcuts import render, redirect
from . forms import PostForm
from datetime import date, time
from . models import Post

# Create your views here.
def HomeView(request):
    post = Post.objects.all()
    
    context = {
        'post':post
    }
    return render(request, 'home.html', context)


def Create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = date.today
            post.updated = date.today
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {
        'form':form
    }
            
    return render(request, 'create.html', context)



def Update(request, pk):
    data = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.updated = date.today
            form.save()            
            return redirect('home')
    else:
        form = PostForm(instance=data)

    context = {
        'form':form
    }
    return render(request, 'update.html', context)