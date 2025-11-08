from django import forms
from django.core.exceptions import ValidationError
from .models import News, Category

def validate_image_size(image):
    """
    Validate that the image size is less than 2MB
    """
    max_size = 2 * 1024 * 1024  # 2MB in bytes
    
    if image.size > max_size:
        raise ValidationError(f'Image size should not exceed 2MB. Current size: {image.size / (1024 * 1024):.2f}MB')
    
    return image

class NewsForm(forms.ModelForm):
    featured_image = forms.ImageField(
        required=False,
        validators=[validate_image_size],
        help_text="Upload an image (max 2MB)"
    )
    
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter article title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your article content here'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief summary of the article (optional)'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name'}),
        }
    
    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')
        
        if image:
            # Check file size
            max_size = 2 * 1024 * 1024  # 2MB
            if image.size > max_size:
                raise forms.ValidationError(
                    f'Image size should not exceed 2MB. Current size: {image.size / (1024 * 1024):.2f}MB'
                )
            
            # Check file type
            allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp']
            if image.content_type not in allowed_types:
                raise forms.ValidationError(
                    'Only JPEG, PNG, GIF, and WebP images are allowed.'
                )
        
        return image

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category name'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category-slug'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Category description (optional)'}),
        }
