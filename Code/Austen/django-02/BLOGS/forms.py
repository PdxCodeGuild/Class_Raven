from django.forms import *
from . import models
from datetime import datetime
class post:
    class new(ModelForm):
        class Meta:
            model = models.Post
            fields = ['title', 'content', 'public', 'edited']
            widgets = {'content': Textarea(attrs={'cols': 25, 'rows': 5}), 'edited': HiddenInput()}
        
        def save(self, blog, commit=True):
            new_post = super(post.new, self).save(commit=False)
            title = self.cleaned_data['title']
            content = self.cleaned_data['content']
            public = self.cleaned_data['public']
            if commit:
                new_post = models.Post.objects.create(blog=blog, title=title, content=content, public=public)
            return new_post
        def update(self, selected_post, commit=True):
            updated_post = models.Post.objects.get(title=selected_post.title)
            updated_post.title = self.cleaned_data['title']
            updated_post.content = self.cleaned_data['content']
            updated_post.public = self.cleaned_data['public']
            updated_post.edited = datetime.now()
            if commit:
                updated_post.save()
            return updated_post