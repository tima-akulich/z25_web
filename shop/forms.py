from django import forms


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
