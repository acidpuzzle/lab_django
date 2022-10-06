from django.forms import *
from django.core.exceptions import ValidationError

from .models import Tag, Post


# class TagForm(Form):
#     title = CharField(max_length=50)
#     slug = CharField(max_length=50)
#
#     title.widget.attrs.update({'class': 'form-control mb-2'})
#     slug.widget.attrs.update({'class': 'form-control mb-2'})
#
#     def clean_slug(self):
#         lower_slug = self.cleaned_data['slug'].lower()
#         print(lower_slug)
#
#         if lower_slug == 'new_tag':
#             raise ValidationError(f"Tag cannot be named `{lower_slug}`.")
#         if Tag.objects.filter(slug__iexact=lower_slug).count():
#             raise ValidationError(f"`{lower_slug}` alredy exist.")
#
#         return lower_slug
#
#     def save(self):
#         print(self.errors)
#         new_tag = Tag.objects.create(
#             title=self.cleaned_data['title'],
#             slug=self.cleaned_data['slug'],
#         )
#         return new_tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control mb-2'}),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control mb-2'}),
            'body': Textarea(attrs={'class': 'form-control mb-2'}),
            'tags': SelectMultiple(attrs={'class': 'form-control mb-2'}),
        }

