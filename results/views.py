from django.shortcuts import render
from . models import Result,Marks

def index(request):
    list_of_results = Result.objects.all()
    return render(request,'index.html',{'list_of_results':list_of_results})

def marks(request):
    return render(request,'result.html')

def validate(request):
    htno = request.POST['htno']
    try:
        dataMarks = Marks.objects.get(htno=htno)
        return render(request,'marks.html',{'dataMarks':dataMarks})
        
    except:
        return render(request,'error.html',{'htno':htno})