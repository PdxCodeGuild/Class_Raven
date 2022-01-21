from .models import BlogPost


from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [ # '__all__'  # can do this if you want allllllll the form fields
            'title',
            'body',
        ]
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control', 'rows':'4'}),
        }