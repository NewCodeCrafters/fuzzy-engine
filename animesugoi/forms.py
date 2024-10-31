from django import forms


from .models import Category, Anime

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = "__all__"
        # fields = ['title', 'category', 'aurthor', 'num_pages']
        # exclude = [""]