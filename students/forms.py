from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile, SkillRequest, Feedback

class RegistrationForm(UserCreationForm):
    skills = forms.CharField(max_length=255, required=True, help_text="List your skills separated by commas")
    expertise = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}), required=True, help_text="Describe your expertise")
    department = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    id_card_number = forms.CharField(max_length=20, required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'skills', 'expertise', 'department', 'email', 'phone_number', 'id_card_number', 'image']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = StudentProfile(
                user=user,
                skills=self.cleaned_data['skills'],
                expertise=self.cleaned_data['expertise'],
                department=self.cleaned_data['department'],
                email=self.cleaned_data['email'],
                phone_number=self.cleaned_data['phone_number'],
                id_card_number=self.cleaned_data['id_card_number'],
                image=self.cleaned_data['image'],
            )
            profile.save()
        return user

class ProfileEditForm(forms.ModelForm):
    skills = forms.CharField(max_length=255, required=True, help_text="List your skills separated by commas")
    expertise = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}), required=True, help_text="Describe your expertise")
    class Meta:
        model = StudentProfile
        fields = ['skills', 'expertise', 'department', 'email', 'phone_number', 'id_card_number', 'image']

class SkillRequestForm(forms.ModelForm):
    class Meta:
        model = SkillRequest
        fields = ['skill']

class FeedbackForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']