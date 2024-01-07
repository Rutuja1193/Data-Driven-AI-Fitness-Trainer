from django import forms

class UserInfoForm(forms.Form):
    age = forms.IntegerField(label='Age')
    weight = forms.FloatField(label='Weight (in kg)')
    height = forms.FloatField(label='Height (in cm)')
    allergies = forms.CharField(label='Allergies', max_length=200)
    is_vegetarian = forms.BooleanField(label='Are you vegetarian?', required=False)


class RecommendationForm(forms.Form):
    age = forms.IntegerField(label='Age')
    weight = forms.FloatField(label='Weight')
    goals = forms.CharField(label='Goals (comma-separated)', widget=forms.TextInput(attrs={'placeholder': 'e.g., Lose Weight, Build Muscle'}))
