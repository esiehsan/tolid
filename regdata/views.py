from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Part
from .forms import PartForm
# from jalali_date import datetime2jalali, date2jalali

# Create your views here.

def homePageView(request):

    return render(request, 'home.html')

def employeeListView(request):
    
    employees = Employee.objects.all()

    context = {
        'employees' : employees ,
        }
    return render(request, 'employees.html', context)

def partListView(request):
    parts = Part.objects.all()

    context = {
        'parts': parts
    }
    return render(request, 'parts.html', context )
    

def create_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_part')
        else:
            return HttpResponse('<h1>ERROR</h1>')
    else:
        lastPart = Part.objects.last()
        form = PartForm(initial={'castDate':lastPart.castDate,
                                 'caster1':lastPart.caster1,
                                 'caster2':lastPart.caster2,
                                 'caster3':lastPart.caster3,
                                 })
        context = {'form': form}
        return render(request, 'create_Part.html', context)
