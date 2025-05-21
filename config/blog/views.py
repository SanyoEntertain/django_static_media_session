from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
import os
from django.conf import settings

# READ
def home(request):
    blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

# DETAIL READ
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

# CREATE
def create(request):
    if request.method == 'POST':
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.content = request.POST['content']
        new_blog.image = request.FILES.get('image')
        new_blog.save()
        return redirect('detail', new_blog.id)
    return render(request, 'new.html')

# 수정 구현.
def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':blog})

def update(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.title = request.POST['title']
        print(type(request.POST.get('file_delete')))
        if request.POST.get('file_delete') == 'on':
            delete_image(blog)
            blog.image = None
        # blog image에 저장하기 전, 파일이 업로드 되었는지 확인
        new_image = request.FILES.get('change_image')
        # check image
        if new_image:
            delete_image(blog)
            blog.image = new_image
        blog.content = request.POST['content']
        blog.save()
        return redirect('detail', blog.id)
    return render(request, 'edit.html')

# image delete function
def delete_image(blog):
    if blog.image:
        img_path = os.path.join(settings.MEDIA_ROOT, blog.image.name)
        if os.path.exists(img_path):
            os.remove(img_path)
    else:
        return False