from .models import Post
from django.contrib import admin
from django import forms


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = "new help text"

    class Meta:
        model = Post
        exclude = ('',)


class PostFormAdmin(admin.ModelAdmin):
    form = PostForm

    # having all the fields like just the line above or
    # having selective fields with below solution

    # fieldsets = (
    #     ('First Section', {
    #         'fields': ('title', 'category'),
    #         'description': 'just a simple description'
    #     }),
    # )


admin.site.register(Post, PostFormAdmin)

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
