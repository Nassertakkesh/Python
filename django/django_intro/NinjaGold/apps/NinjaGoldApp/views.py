from django.shortcuts import render, redirect
import random 
from time import gmtime, strftime
		# notice the import!


def index(request):
    if type(request.session.get('counter')) is int:
        print('key exists!')
        
    else:
        print("key 'counter' does NOT exist")
        request.session['counter'] =0

    if request.session.get('newStr'):
        print('newStr exists!')
        
    else:
        print("key 'newStr' does NOT exist")
        request.session['newStr'] = []

 

    return render(request, "NinjaGoldApp/index.html")


def process_money(request):

    if request.method == "POST" and request.POST.get('farm'):
        num1 = random.randint(10, 20) 
        print(num1)
        request.session['counter'] += int(num1)
        name ='farm'
        # time = datetime.datetime.now()

    elif request.method == "POST" and request.POST.get('cave'):
        num1 = random.randint(5, 10) 
        request.session['counter'] += int(num1)
        name ='cave'
        # time = datetime.datetime.now()

    elif request.method == "POST" and request.POST.get("house"):
        num1 = random.randint(2, 5) 
        request.session['counter'] += int(num1)
        name = 'house'
        # time = datetime.datetime.now()
  	
    elif request.method == "POST" and request.POST.get('casino'):
        num1 = random.randint(-50, 0) 
        print('hi')
        request.session['counter'] += int(num1)
        name =  'casino'
        # time = datetime.datetime.now()

    num = num1

    # append(request.session['newStr']) += num
    request.session["newStr"].append({
        "num": num, 
        "location" : name,
        "time":  strftime("%Y-%m-%d%H:%M %p", gmtime())
    })
    print(request.session["newStr"][0])

    return redirect('/')
    
