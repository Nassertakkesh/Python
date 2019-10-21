from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    

@app.route('/play')  
def hello_world():
    return render_template('index.html')  

@app.route('/play/<integ>/<coloring>')  
def blocks(integ, coloring):
    return render_template("index.html", times = int(integ), colors = coloring)
    

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  # Run the app in debug mode.
    # import statements, maybe some other routes
   