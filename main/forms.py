from django import forms

class GeneratorOptions(forms.Form):    
    Length = forms.IntegerField(label="Password Length (minimum 4)", min_value=4, max_value=30)
    ContainsUpper = forms.BooleanField(label="Must contain Upper case", required=False)
    ContainsNumber = forms.BooleanField(label="Must contain number", required=False)
    ContainsSpecial = forms.BooleanField(label="Must contain special character", required=False)