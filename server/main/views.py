from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# TODO Delete whis
def card_edit(request):
    return render(request, 'personal-card.html')
