from django.shortcuts import render, redirect
from .models import PostModel, Comments
from .forms import PostModelForm, PostModelUpdateFrom, CommentsFrom
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    context = {}
    context['title'] = "Home | Post Scribers"
    """     Add Post """
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
        else:
            return redirect('login')
    form = PostModelForm()
    context['form'] = form
    """     Show Post """
    context['post'] = PostModel.objects.all()[::-1]
    return render(request, 'blog/index.html', context)
@login_required
def post_details(request, pk):
    context = {}
    context['title'] = "Post Details | Post Scribers"
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        comment_form = CommentsFrom(request.POST)
        if comment_form:
            instance = comment_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('post-detail', pk=post.id)
    comment_form = CommentsFrom()
    context['comment_form'] = comment_form
    context['post'] = post
    return render(request, 'blog/post_details.html', context)
@login_required
def post_edit(request, pk):
    context = {}
    context['title'] = "Post Edit | Post Scribers"
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        form = PostModelUpdateFrom(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.id)
    form = PostModelUpdateFrom(instance=post)
    context['form'] = form
    context['post'] = post
    return render(request, 'blog/post_edit.html', context)
@login_required
def post_delete(request, pk):
    context = {}
    context['title'] = "Post Delete | Post Scribers"
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('index')
    context['post'] = post
    return render(request, 'blog/post_delete.html', context)