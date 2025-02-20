import pprint
from .models import Post, Category
from django.contrib import admin
from django import forms


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = "new help text"

    class Meta:
        model = Post
        exclude = ('',)

    def clean(self):
        title = self.cleaned_data.get('title')
        if title.startswith('N'):
            raise forms.ValidationError('this value is not acceptable')
        return super().clean()


class PostFormAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostFormAdmin)
admin.site.register(Category)


# ================================================
# EXTRA POINST

# When to Use a Custom ModelForm in Django Admin?
# _Add Custom Validation:
# def clean_title(self):
#     title = self.cleaned_data['title']
#     if len(title) < 5:
#         raise forms.ValidationError("Title must be at least 5 characters long")
#     return title

# the hierarchy for deciding which fields to be in admin panel is:
# fieldsets in modelAdmin
# fields in modelAdmin
# ModerlForm.Meta.fields
