from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt    #handled in Middleware level

from .models import Employee
from .forms import EmployeeForm

def index(request):
    queryset = cache.get('emp_objects')
    if queryset is None:
        queryset = Employee.objects.all().values()
        cache.set('emp_objects', queryset)
    return JsonResponse(list(queryset), safe=False)

def show(request, id):
    try:
        queryset = Employee.objects.get(pk=id)
        return JsonResponse(queryset.json())
    except Employee.DoesNotExist:
        return JsonResponse({
            'message': 'Employee does not exists'
        }, status=404)


# @csrf_exempt
def store(request):
    if request.method == "POST":
        eform = EmployeeForm(request.POST)  
        if eform.is_valid():
            eform.save()
            return JsonResponse({
                'message': 'Employee Details added'
            })
        else:
            return JsonResponse(eform.errors, status=415)
    return JsonResponse({
        'message': 'Method Not Supported'
    }, status=405)


# @csrf_exempt
def update(request, id):
    try:
        emp = Employee.objects.get(pk=id)
        if request.method == "POST":
            eform = EmployeeForm(request.POST, instance=emp)  
            if eform.is_valid():
                eform.save()
                return JsonResponse({
                    'message': 'Employee Details updated'
                })
            else:
                return JsonResponse(eform.errors, status=415)
    except Employee.DoesNotExist:
        return JsonResponse({
            'message': 'Employee does not exists'
        }, status=404)
    return JsonResponse({
        'message': 'Method Not Supported'
    }, status=405)


def destroy(request, id):
    try:
        Employee.objects.get(pk=id).delete()
        return JsonResponse({
            'message': 'Employee details removed'
        })
    except Employee.DoesNotExist:
        return JsonResponse({
            'message': 'Employee does not exists'
        }, status=404)