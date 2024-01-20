from django import forms
from .models import Profile, BlogPost
from django import forms
from ckeditor.widgets import CKEditorWidget


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
