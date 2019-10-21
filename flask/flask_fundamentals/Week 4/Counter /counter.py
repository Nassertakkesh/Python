from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

#   if session.get('counter') not None:

@app.route('/' )
def hello_worl():
    
    if type(session.get('counter')) is int:
        print('key exists!')
    else:
        print("key 'counter' does NOT exist")
        session['counter'] =0

    session['counter'] += 1
    return render_template("index.html")

@app.route('/clear')
def clearSession():
    session.clear()
    return redirect('/')

# @app.route('/result', methods  = ['POST', 'GET'])
# def results():
#     print(request.form["names"])
    
#     return render_template("results.html" )
   


if __name__ == "__main__":
    app.run(debug=True)

