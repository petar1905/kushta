from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from watergathering.models import WaterGatherDate
from datetime import datetime, timedelta
from watergathering.forms import DateForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
  template = loader.get_template('water_view.html')
  results = []
  
  for i in range(7):
    day = datetime.today()+timedelta(days=i)
    record = WaterGatherDate.objects.filter(date=day)
    try:
      results.append(record[0])
    except IndexError:
      newRec = WaterGatherDate.objects.create(date=day, 
      gatherer='Никой', completion=False)
      newRec.save()
      results.append(newRec)
  context = {'records': results}
  return HttpResponse(template.render(context, request))

@login_required
def single(request, id):
  template = loader.get_template('water_single.html')
  record = WaterGatherDate.objects.get(id=id)
  context = {'record': record}
  return HttpResponse(template.render(context, request))
# Create your views here.

@login_required
def single_edit(request, id):
  record = WaterGatherDate.objects.get(id=id)
  if request.method == 'POST':
    form = DateForm(request.POST)
    if form.is_valid():
      completion = form.cleaned_data['completion']
      gatherer = form.cleaned_data['gatherer']
      record.completion = completion
      record.gatherer = gatherer
      record.save()
      
      return HttpResponseRedirect('/water/'+str(id))
  init = {
    'completion': record.completion,
    'gatherer': record.gatherer
  }
  form = DateForm(initial=init)
  template = loader.get_template('water_single_edit.html')
  context = {'record': record, 'form': form}
  return HttpResponse(template.render(context, request))