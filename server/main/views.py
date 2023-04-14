from django.shortcuts import render


def index(request):
    return render(request, 'list_employeers.html')


# TODO Delete whis
def card_edit(request):
    return render(request, 'edit_employeer.html')
