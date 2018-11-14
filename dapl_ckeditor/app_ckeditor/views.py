from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm


# Create your views here.

def home(request):
    return render(request, 'app_ckeditor/home.html')


def blog(request):
    if request.method == 'GET':
        form = BlogForm()
        return render(request, 'app_ckeditor/blog.html', {"form": form})
    elif request.method == 'POST':
        print(request.FILES)
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.featured_image = form.cleaned_data['featured_image']
            instance.save()
            return HttpResponseRedirect(reverse_lazy('app_ckeditor:blog_list'))


def blog_list(request):
    blogs = Blog.objects.all()
    print(blogs)
    for blog in blogs:
        print(blog.featured_image)
    return render(request, 'app_ckeditor/blog_list.html', {"blogs": blogs})

def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'app_ckeditor/blog_details.html', context)


def blog_edit_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('app_ckeditor:blog_list'))
    else:
        return render(request, 'app_ckeditor/blog_edit.html', {"form": form})


def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return HttpResponseRedirect(reverse_lazy('app_ckeditor:blog_list'))
