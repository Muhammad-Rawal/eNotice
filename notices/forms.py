from django import forms
from .models import Notice

class NewNoticeForm(forms.ModelForm):

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Write your message here...'}
        ),
        max_length=2000,
        help_text='The max length of the text is 2000.'
    )

    class Meta:
        model = Notice
        fields = ['title', 'message', 'image', 'video', 'document']
        labels = {
            'title': 'Title',
            'image': 'Image (SVG, PNG, JPG, GIF up to 800x400px)',
            'video': 'Video (MP4, MOV, AVI up to 50MB)',
            'document': 'Document (PDF, DOCX, TXT up to 5MB)'
        }
        help_texts = {
            'image': 'Allowed formats: SVG, PNG, JPG, GIF. Maximum resolution: 800x400 pixels.',
            'video': 'Allowed formats: MP4, MOV, AVI. Maximum file size: 50MB.',
            'document': 'Allowed formats: PDF, DOCX, TXT. Maximum file size: 5MB.'
        }
