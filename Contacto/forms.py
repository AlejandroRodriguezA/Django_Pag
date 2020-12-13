from django import forms


class ContactoForm(forms.Form):
    error_css_class = 'error'
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Your Name'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Subject'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control','placeholder' : 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control','row' : '5','placeholder' : ' Message'}))
    
    def clean(self):
        cleaned_data = super(ContactoForm, self).clean()
        name=cleaned_data.get('name')
        subject = cleaned_data.get('subject')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        if not name and not subject and not email and not message:
            raise forms.ValidationError('You have to write something!')

        
        


