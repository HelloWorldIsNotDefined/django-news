from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        widget=forms.TextInput(
        attrs={'class':'form-control','style':'width:500px;', 'placeholder':'search'}
        )
    )