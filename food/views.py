from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime, timedelta
from watergathering.forms import DateForm
from django.contrib.auth.decorators import login_required
from food.models import FoodDate
from .forms import FoodDateForm


@login_required
def foodview(request):
  template = loader.get_template('food_view.html')
  results = []

  for i in range(7):
    day = datetime.today()+timedelta(days=i)
    record = FoodDate.objects.filter(date=day)
    try:
      results.append(record[0])
    except IndexError:
      newRec = FoodDate.objects.create(date=day, 
      lunch='Не е обявено', dinner='Не е обявено')
      newRec.save()
      results.append(newRec)
    context = {'records': results}
  return HttpResponse(template.render(context, request))

@login_required
def single_food(request, id):
  template = loader.get_template('food_single.html')
  record = FoodDate.objects.get(id=id)
  context = {'record': record}
  return HttpResponse(template.render(context, request))
  
@login_required
def single_food_edit(request, id):
  record = FoodDate.objects.get(id=id)
  if request.method == 'POST':
    form = FoodDateForm(request.POST)
    if form.is_valid():
      lunch = form.cleaned_data['lunch']
      dinner = form.cleaned_data['dinner']
      record.lunch = lunch
      record.dinner = dinner
      record.save()
      
      return HttpResponseRedirect('/food/'+str(id))
  init = {
    'lunch': record.lunch,
    'dinner': record.dinner
  }
  form = FoodDateForm(initial=init)
  template = loader.get_template('food_single_edit.html')
  context = {'record': record, 'form': form}
  return HttpResponse(template.render(context, request))
  

# Create your views here.
