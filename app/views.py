# from django.shortcuts import render

# Create your views here.
# •	/ — домашняя страница, содержит список доступных страниц;
# •	current_time/ — показывает текущее время в любом удобном вам формате;
# •	workdir/ — выводит содержимое рабочей директории.

# import datetime


from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir
from datetime import datetime

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


#
def time_view(request):
    #     # обратите внимание – здесь HTML шаблона нет,
    #     # возвращается просто текст
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    # raise NotImplemented
    result = '\n'.join(listdir(path='.'))
    return HttpResponse(result)















# MY
# def home_view(request):
#     return HttpResponse("Список доступных страниц")
#
# def current_time(request):
#     return HttpResponse(datetime.datetime.now())
#
# def workdir(request):
#     return HttpResponse("???")