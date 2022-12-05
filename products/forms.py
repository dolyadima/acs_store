from django import forms


class ProdFilterForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    category = forms.CharField(label='category', max_length=25)
    price = forms.IntegerField(label='price')
    shop = forms.CharField(label='shop', max_length=100)
