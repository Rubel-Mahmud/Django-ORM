from django.forms import ModelForm
from blog.models import Blog

class BlogAddForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'tagline']