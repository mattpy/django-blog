from django.shortcuts import render, HttpResponse

items = [
    {'id': 1, 'title': 'Brave New World', 'author': 'Frank West'},
    {'id': 2, 'title': 'Gone with the Wind', 'author': 'Swimming Trunks'},
    {'id': 3, 'title': 'Ender\'s Game', 'author': 'Keyboard'}
]


def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    context = {'posts': items}
    return render(request, 'blog/posts.html', context)


def post(request, slug):
    context = {'id': slug}
    return render(request, 'blog/post.html', context)
