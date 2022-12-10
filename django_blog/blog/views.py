from django.shortcuts import render
# from django.http import HttpResponse : no longer being used, hence commented out.
# Create your views here.


def home(request):
    # return HttpResponse('<h1> Blog Home</h1>')
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
    # return HttpResponse('<h1> Blog About</h1>')
