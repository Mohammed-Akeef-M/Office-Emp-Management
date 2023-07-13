from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, "home.html")

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, "all_emp.html", context)

def add_emp(request):
    if request.method=='POST':
        First_name = request.POST['First_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        new_emp = Employee(First_name=First_name, last_name=last_name, salary=salary, dept_id=dept, bonus=bonus, role_id=role,
                 phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
        
    elif request.method=='GET':
        return render(request, "add_emp.html")
    else:
        return HttpResponse('An exception occured, Employee has not been added ')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter a valid emp id")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }

    return render(request, "remove_emp.html", context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(First_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name__icontains =dept)
        if role:
            emps=emps.filter(role__name__icontains =dept)
        context={
            'emps': emps
        }    
        return render(request, "all_emp.html", context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An exception occured ')
