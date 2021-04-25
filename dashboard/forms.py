from django import forms
from .models import Room, News, Comment


class StaffLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if username in Account.objects.all():
    #         return username
    #     else:
    #         raise ValidationError('')


class RoomForm(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control select2',
        'multiple': True
    }))

    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_type': forms.Select(attrs={
                'class': 'form-control select2',
                'placeholder': 'room type'
            }),
            'room_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'room no'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'price'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            }),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['features'].widget.attrs.update({
            'class': 'form-control select2 feature-select',
            'multiple': 'multiple'
        })


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description' 
        }),
           
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            }),

            'Created By': forms.Select(attrs={
                'class': 'form-control select2',
            })

        }
        
class NewsCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('full_name','email', 'news','comment')
