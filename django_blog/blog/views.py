from django.shortcuts import render
# from django.http import HttpResponse : no longer being used, hence commented out.
# Create your views here.

# This is a list of dictionaries
posts = [
    {  # This is basically the first post
        'author': 'Sabyasachi',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'December 10, 2022'
    },
    {  # Second (mock) blog post
        'author': 'Still Sabyasachi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 11, 2022'

    }


]


def home(request):
    context = {
        'posts': posts
    }
    # return HttpResponse('<h1> Blog Home</h1>')
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    # return HttpResponse('<h1> Blog About</h1>')
