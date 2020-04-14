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


 # 3. Lesson / 24.03.2020
### Documentation
- https://en.wikipedia.org/wiki/Cross-site_request_forgery
- https://docs.djangoproject.com/en/3.0/topics/forms/
- https://docs.djangoproject.com/en/3.0/ref/templates/builtins/
- https://docs.djangoproject.com/en/3.0/howto/static-files/

### Homework 3
1. Добавить bootstrap статику в проект. https://getbootstrap.com/
2. Используя bootstrap привести сайт к нормальному виду
На Странице сайта должен быть header в котором будут ссылки на разные страницы,
Header должен содержать в себе кнопки Products | Categories
В Products должен быть список всек товаров. Оформить в виде сетки (взять из bootstrap)
Products должены поддерживать пагинацию https://docs.djangoproject.com/en/3.0/topics/pagination/
На странице Categories должна быть страница в виде двух колонок.
Список категорий| Товары (в виде таблицы как на странице Products)

PS: таблицы не использовать

 # 4. Lesson / 31.03.2020
### Documentation
- https://docs.djangoproject.com/en/2.2/topics/http/middleware/ - мидлвари
- https://docs.djangoproject.com/en/3.0/topics/class-based-views/ - cbv

### Homework 4
1. Добавить страницу с регистрацией
2. Создать middleware, которая будет писать в базу 500 ошибки приложения(Если такие будут). (Придумать модель куда будете писать)
Добавить модель в админку. Добавить поиск, фильтрацию по полям которые придумаете.
3. Расширяем возможности нашего сайта, добавить возможность добавления товара в корзину. + добавить страницу с корзиной на сайте.

PS: таблицы не использовать

 # 5. Lesson / 04.04.2020
### Documentation
- https://devcenter.heroku.com/articles/getting-started-with-python#set-up - heroku
- https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/ - django commands
- https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/ - переменные

### Homework 5
1. Привести к красивому виду кнопку "добавить в корзину", привести к нормальному виду страницу с корзиной
2. Добавить страницу оформления заказа (заполнение данных и отправка заказа на сервер + добавить прсмотр заказа в админке)
3. Задеплоить на heroku (к ПР приложить ссылку)

 # 6. Lesson / 07.04.2020
### Documentation
- https://docs.djangoproject.com/en/3.0/topics/i18n/translation/ - переводы
- https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html - celery
- https://habr.com/ru/post/461775/ - зачем celery?

### Homework 6
1. Сдедать перевод сайта/админки на русский язык
2. При регистрации пользователя добавить email на форму
3. Создать периодическую задачу, которая раз в неделю (в понедельник в 9 утра), рассылает всем пользователям 
email о новых товарах которые поступили в продажу

PS: https://docs.djangoproject.com/en/3.0/topics/email/

PSS: кто сделает реальную отправку письма на реальную почту тому +

 # 7. Lesson / 10.04.2020
### Documentation
- https://ru.wikipedia.org/wiki/API - что такое API
- https://habr.com/ru/post/351890/ - Best Practices
- https://www.django-rest-framework.org/

### Homework 7
0. Создать API для регистрация пользователя
1. Создать API на получения списка продуктов
2. API для добавления товара в корзину
3. API для оформления заказа
4. Задеплоить на Heroku

 # 8. Lesson / 14.04.2020
### Documentation
- https://docs.djangoproject.com/en/3.0/topics/testing/overview/
- https://habr.com/ru/post/141209/

### Homework 8
1. Покрыть тестами приложение api
