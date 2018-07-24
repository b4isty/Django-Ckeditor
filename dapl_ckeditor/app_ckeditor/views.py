from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm


# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'app_ckeditor/home.html', {"blogs": blogs})


def blog(request):
    if request.method == 'GET':
        form = BlogForm()
        return render(request, 'app_ckeditor/blog.html', {"form": form})
    elif request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse_lazy('app_ckeditor:home'))


def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'app_ckeditor/blog_details.html', context)


def blog_edit_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('app_ckeditor:home'))
    else:
        return render(request, 'app_ckeditor/blog_edit.html', {"form": form})
