from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Hari',
        'title' : 'Learning Django',
        'content' : 'Learning Django from Corey Schafer',
        'date' : 'Dec 7, 2023'
    },
        {
        'author' : 'Ken',
        'title' : 'Learning DevOps',
        'content' : 'Learning Django from Abhishek Veeramalla',
        'date' : 'Dec 6, 2023'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def contact(request):
    return HttpResponse('<h1> Contact Info </h1>')