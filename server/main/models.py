from django.db import models


class Employees(models.Model):
    sexs = [
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    ]
    lastname = models.CharField(max_length=30, verbose_name='Фамилия')
    firstname = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Отчество')
    post = models.ForeignKey('Posts', null=True, on_delete=models.SET_NULL, verbose_name='Должность')
    age = models.IntegerField(verbose_name='Возраст')
    gender = models.CharField(max_length=10, choices=sexs, verbose_name='Пол')

    def __str__(self):
        return f'{self.lastname} {self.firstname} {self.surname}'

    class Meta:
        ordering = ['lastname', 'firstname', 'surname']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Posts(models.Model):
    categories = [
        ('Специалист', 'Специалист'),
        ('Рабочий', 'Рабочий'),
        ('Служащий', 'Служащий'),
    ]
    post = models.CharField(max_length=30, verbose_name='Должность')
    category = models.CharField(max_length=15, choices=categories, verbose_name='Категория')

    def __str__(self):
        return self.post

    class Meta:
        ordering = ['post']
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'