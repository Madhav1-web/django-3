from django.shortcuts import render, get_object_or_404
from .models import blogs

def all_blogs(request):
	blog=blogs.objects.all()
	blog_count=blogs.objects.count

	return render(request, 'blog/all_blogs.html', {'blog':blog, 'blog_count':blog_count})

def detail(request, blog_id):
	blog=get_object_or_404(blogs, pk=blog_id)
	return render(request, 'blog/details.html', {'blog':blog})


