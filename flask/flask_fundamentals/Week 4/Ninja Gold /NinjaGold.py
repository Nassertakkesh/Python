from flask import Flask, render_template, redirect, request, session
import random 
random.randint(1, 100) 	

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

activities = []
@app.route('/')
def index():
    session['activity'] = " "
    if type(session.get('counter')) is int:
        print('key exists!')
        
    else:
        print("key 'counter' does NOT exist")
        session['counter'] =0
    return render_template("index.html")
      

@app.route('/users', methods=['POST'])
def hello_worl():
    request.form.get('farm')
    if request.form.get('farm'):
        num1 = random.randint(10, 20) 
        session['counter']  += num1
        session['activity'] += str(num1)
        print(session['activity'])

    elif request.form.get('cave'):
        num2 =  random.randint(5,10)
        session['counter'] += num2
        session['activity'] += str(num2)
        print(session['activity'])
    

    elif request.form.get('house'):
        num3 = random.randint(2,5)
        session['counter'] +=  num3
        session['activity'] += str(num3)
        print(session['activity'])


    elif request.form.get('casino'):
        num4 = random.randint(-50, 50) 
        session['counter'] += num4
        session['activity'] += str(num4)
        print(session['activity'])

    return redirect('/')

# @app.route('/reset', methods=['GET', 'POST'])
# def reset():
#     session.clear()
#     return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)
