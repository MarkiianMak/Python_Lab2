

from django import forms
from courses.models import Course  

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courseName', 'duration', 'category'] 
        widgets = {
            'courseName': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
