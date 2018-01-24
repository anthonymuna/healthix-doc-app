from django import forms
from .simple_search import search_form_factory
from .models import Search
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs={
            'class':'form-control'
        }
        self.fields['email'].widget.attrs={
            'class':'form-control'
        }
        self.fields['password'].widget.attrs={
            'class':'form-control'
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()

SearchForm = search_form_factory(Search.objects.all(),
                                 ['^first_name', 'last_name', 'mobile_num'])