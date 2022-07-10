from django.forms import ModelForm, TextInput, Textarea
from home.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'telegram', 'message']
        widgets = {
            'first_name': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ism *'}),
            'last_name': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Familiya *'}),
            'phone': TextInput(
                attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Aloqa uchun telefon raqam *'}),
            'telegram': TextInput(attrs={'type': 'text', 'class': 'form-control',
                                         'placeholder': 'Telegram lichka yoki telegram telefon raqami *'}),
            'message': Textarea(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Sizning xabaringiz *'})
        }
