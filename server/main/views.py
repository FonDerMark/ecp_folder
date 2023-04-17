from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def employeers_list(request):
    return render(request, 'list_employeers.html')


def employeer_edit(request):
    return render(request, 'edit_employeer.html')


def employeer_add(request):
    return render(request, 'add_new_employeer.html')


def posts_list(request):
    return render(request, 'list_posts.html')


def post_edit(request):
    return render(request, 'edit_post.html')


def post_add(request):
    return render(request, 'add_new_post.html')
