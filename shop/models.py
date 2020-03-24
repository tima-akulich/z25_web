from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('1', 'Category_name_1'),
        ('2', 'Category_name_2'),
        ('3', 'Category_name_3'),
        ('4', 'Category_name_4')
    ]
    number = models.CharField(max_length=4)
    name = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    company = models.ForeignKey(Company, to_field='name', on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}, {self.number}, {self.quantity}, {self.company}'


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=90)
    orders = models.ManyToManyField(Product, through='Order')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Order(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer_name.first_name},' \
               f' {self.product_name.name},' \
               f' {self.product_name.quantity}'
