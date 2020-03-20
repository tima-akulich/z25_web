# 1. Lesson / 19.03.2020
### Documentation
- https://ru.wikipedia.org/wiki/Model-View-Controller
- https://djangobook.com/mdj2-django-structure/
- https://docs.djangoproject.com/en/3.0/intro/tutorial01/ - туториал
- https://docs.djangoproject.com/en/3.0/topics/db/models/

### Books
- https://github.com/prasad01dalavi/python_books/blob/master/Daniel%20Greenfeld%20-%20Two%20Scoops%20of%20Django%201.11%20-%202017.pdf
хорошая книга по Django

### Homework 1
0. Почитать про джангу. Оперировать терминами - проект, приложения, model, view, template.

1. Создать отдельное приложение в этом проекте и назвать его test_app.
В этом приложении необходимо описать все модели из занятия lesson12 использую Django ORM.
Добавить миграции.

2. Создать приложение try_mtv
 - Создать template, на котором будет форма для ввода текста и кнопка
 - Описать view, которая будет обрабатывать запросы с формы.
 - В качестве данных с формы приходит строка, которая содержит строчку вида - '((hello))(((world)())())'
 - на view необходимо провалидириовать эту строчку на правильное расставление скобок
 - view в ответ рендерит на шаблон переменную, которая содержит информацию о том, верно ли расставлены скобки
 
 
 # 2. Lesson / 20.03.2020
### Documentation
- https://docs.djangoproject.com/en/3.0/topics/db/models/
- https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
- https://docs.djangoproject.com/en/3.0/ref/templates/builtins/

### Homework 2
1. В приложении shop описать все необходимые модели для работы нашего "Amazing" магазина (придумать какие нужны, и как связаны будут)
2. Описать несколько теплейтов:
- Темплейт который выводит список всех товаров (внешний вид на ваше усмотрение)
- Темплейт который вывод детальную информацию о товаре
3. Добавить в admin панель все модели из задания (1) (настроить колонки, фильтры, поиск)

PS: добавить css, чтобы страница не была белым полотном.