from django import forms

class DateForm(forms.Form):
  gatherer = forms.CharField(
    label='Изпълнител', 
    max_length=100,
    required=True
  )
  completion = forms.BooleanField(
    label='Изпълнено',
    required=False
  )