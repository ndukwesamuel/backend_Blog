from django.forms import ModelForm
from django import forms

from Home.models import  Post                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  





class Post_Form(ModelForm):
    class Meta:
        model= Post
        fields= '__all__'
        # exclude =  ['user']

 
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'title here'}),        
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class Post_edit_Form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'title here'}),        
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
