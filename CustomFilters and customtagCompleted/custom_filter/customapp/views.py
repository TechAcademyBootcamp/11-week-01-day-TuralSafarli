from django.shortcuts import render
from datetime import date, datetime


# Create your views here.

def custom_function(request):

    datestr= '12-17-2019'
    mystr = "Tech academy"
    fdate= datetime.strptime(datestr, "%m-%d-%Y").date()


    context={
       
        'date': fdate,
        'mystr': mystr,
        

    }

    return render (request, 'custom.html', context)


