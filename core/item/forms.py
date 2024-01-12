from django import forms
from .models  import  Item,Category


class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image',)
        
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=False)    
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter name of product ','class':'form-control'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description of product ','class':'form-control'}))    
    price=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter price of product ','class':'form-control'}))    
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))    