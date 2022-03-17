from django import forms

import core.models


class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False, widget=forms.Textarea)
    min_pages = forms.IntegerField(label='Количество страниц', required=False, help_text='Минисмальное количество страниц')

    def clean(self):
        raise forms.ValidationError('Ошибка!')


class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'
