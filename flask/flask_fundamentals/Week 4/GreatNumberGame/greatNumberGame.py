from flask import Flask, render_template, redirect, request, session
import random 
random.randint(1, 100) 	

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if type(session.get('random')) is int:
        print('key exists!')
    else:
        session['random'] = random.randint(1, 100)
        print(session['random'])

    if type(session.get('counter')) is int:
        print('key exists!')
    else:
        print("key 'counter' does NOT exist")
        session['counter'] =0
    return render_template("index.html")
    
@app.route('/users', methods=['POST'])
def hello_worl():
    print(request.form)
    guess = request.form['name']
    session['counter'] += 1
    print(session)

    if session['counter'] >= int(5):
        print('HIGH')
        return redirect("/loser")
    elif int(guess) > int(session['random']):
        print('HIGH')
        return redirect("/tooHigh")
    elif int(guess) < int(session['random']):
        return redirect("/tooLow")
    elif int(guess) == int(session['random']):
        return redirect("/youWin")
    
    
    # return render_template("index.html", name_on_template=name_from_form)

@app.route('/loser', methods=['GET'])
def loser():
    session.clear()
    return render_template("Loser.html")

@app.route('/tooLow', methods=['GET'])
def tooLow():
    print('LOW')
    return render_template("tooLow.html")

@app.route('/tooHigh', methods=['GET'])
def tooHigh():
    print('HIGH')
    return render_template("tooHigh.html")

@app.route('/youWin', methods=['GET'])
def youWin():
    session.clear()
    return render_template("youWin.html")


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    return redirect("/")
    
   
# @app.route('/clear')
# def clearSession():
#     session.clear()
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name_from_form = request.form['name']
#     return render_template("show.html", name_on_template=name_from_form)