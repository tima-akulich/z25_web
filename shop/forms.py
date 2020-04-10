from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from shop.models import Product, Order, BasketItem


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'some-class'}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'email')


class BasketEditForm(forms.Form):
    product_id = forms.IntegerField(required=True)

    def clean_product_id(self):
        product_id = self.cleaned_data['product_id']
        if not Product.objects.filter(id=product_id).exists():
            raise forms.ValidationError('Invalid product ID')
        return product_id


class CardForm(forms.Form):
    NUMBER_LENGTH = 16

    from_card = forms.CharField(required=True)
    to_card = forms.CharField(required=True)
    number = forms.IntegerField(required=True)

    def clean_number(self):
        if self.cleaned_data['number'] < 10:
            raise forms.ValidationError('Number must be > 10')
        return self.cleaned_data['number']

    def _clean_card_number(self, number):
        card_number = number.replace(' ', '')
        if len(card_number) != self.NUMBER_LENGTH:
            raise forms.ValidationError(
                f'Card number length must be equal to {self.NUMBER_LENGTH}'
            )
        return card_number

    def clean_from_card(self):
        return self._clean_card_number(self.cleaned_data['from_card'])

    def clean_to_card(self):
        return self._clean_card_number(self.cleaned_data['to_card'])


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'published', 'value')


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('address', )


class BasketItemForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ('count', )


