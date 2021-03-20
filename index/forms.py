from django import forms
from .models import Notice

class NoticeForm(forms.NoticeForm):

    class Meta:
        model = Movie
        fields = '__all__'