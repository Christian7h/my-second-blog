from django import forms
from .models import Profile, BlogPost
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.core.mail import send_mail
from smtplib import SMTPException

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image','text','description')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
            'text': CKEditorWidget(attrs={'class':'form-control', 'placeholder':'Text of the Blog'}), # Utilizar CKEditorWidget para el campo 'text'
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description of the Blog'}),
        }

class ContactForm(forms.Form):

    name = forms.CharField(max_length=100)

    email = forms.EmailField()

    message = forms.CharField(widget=forms.Textarea)


    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        subject = f'Contact Form: {name}'
        message_body = f'From: {name}\nEmail: {email}\nMessage:\n{message}'
        email_from = "tucorreo@gmail.com"  # Reemplaza con tu dirección de correo
        recipient_list = ['tucorreo@gmail.com']  # Reemplaza con la dirección de correo destino

        try:
            send_mail(subject, message_body, email_from, recipient_list, fail_silently=False)
        except Exception as e:
            print(f"Error al enviar el correo: {e}")