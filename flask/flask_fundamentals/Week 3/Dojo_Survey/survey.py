from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def hello_worl():
    return render_template("index.html")

@app.route('/result', methods  = ['POST', 'GET'])
def results():
    print(request.form["names"])
    name = request.form['names']
    location = request.form['location']
    favlanguage = request.form['favlang']
    comments = request.form['comments']
    return render_template("results.html", favlang =favlanguage, location= location, name= name, comments = comments)
   

if __name__ == "__main__":
    app.run(debug=True)


