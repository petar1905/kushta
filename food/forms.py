from django import forms

class FoodDateForm(forms.Form):
  lunch = forms.CharField(
    label='Обяд', 
    max_length=100,
    required=True
  )
  dinner = forms.CharField(
    label='Вечеря', 
    max_length=100,
    required=True
  )