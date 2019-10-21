from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d", gmtime()),
        "clock": strftime("%H:%M %p", gmtime())
    }
    return render(request,'timeDisplayApp/index.html', context)