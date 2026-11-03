from django import forms
from .models import Review, Product

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product_name', 'image', 'review_text']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



