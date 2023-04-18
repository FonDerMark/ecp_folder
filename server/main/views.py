from django.shortcuts import render


def index(request):
    """
    Функция для главной страницы.
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: html страницу с главной страницей.
    """
    return render(request, 'index.html')


def employeers_list(request):
    """
    Функция для страницы со списком работников.
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: html страницу со списком работников.
    """
    return render(request, 'list_employeers.html')


def employeer_edit(request):
    """
    Функция для страницы редактирования работника.
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: html страницу с формой редактирования работника.
    """
    return render(request, 'edit_employeer.html')


def employeer_add(request):
    """
    Функция для страницы добавления нового работника.
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: html страницу с формой добавления нового работника.
    """
    return render(request, 'add_new_employeer.html')


def posts_list(request):
    """
    Функция для страницы со списком должностей.
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: html страницу со списком должностей.
    """
    return render(request, 'list_posts.html')


def post_edit(request):
    """
    Функция для страницы редактирования должности.
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: html страницу с формой редактирования должности.
    """
    return render(request, 'edit_post.html')


def post_add(request):
    """
    Функция для страницы добавления нового должности.
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: html страницу с формой добавления нового должности.
    """
    return render(request, 'add_new_post.html')
