from django import forms
from .models import Student


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label="Your name")
    email = forms.EmailField(required=True, label="Your email")
    message = forms.CharField(
        widget=forms.Textarea, required=True, min_length=10, label="your message"
    )


class StudentForm(forms.ModelForm):
    # meta class tells django which model to use and which fileds
    # should appear in the forms
    class Meta:
        model = Student
        fields = ["name", "email", "age", "department"]
        labels = {
            "name": "Students name",
            "email": "Email address",
            "age": "Age",
            "departmet": "Department",
        }

        widgets = {"age": forms.NumberInput(attrs={"min": 1, "max": 120})}

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 1 or age > 120:
            raise forms.ValidationError("Age must be between 1 -120")

        return age
