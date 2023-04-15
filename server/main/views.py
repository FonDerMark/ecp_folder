from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def list_employeers(request):
    return render(request, 'list_employeers.html')


def list_posts(request):
    return render(request, 'list_posts.html')


def card_edit(request):
    return render(request, 'edit_employeer.html')
