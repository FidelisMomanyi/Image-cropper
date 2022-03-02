from django import forms

CATEGORIES =( 
    ("1", "personal"), 
    ("2", "Facebook"), 
    ("3", "Snapchat"),   
    ("4", "Instargram"), 
)

class ImagesForm(forms.Form):
    image = forms.ImageField(required=True) 
    imagename = forms.CharField(required=True)
    description = forms.CharField(required=True)
    locaton = forms.CharField(required=True)
    category = forms.ChoiceField(choices=CATEGORIES, required=True)
