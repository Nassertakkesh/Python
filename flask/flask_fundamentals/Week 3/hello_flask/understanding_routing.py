from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    

@app.route('/')  
def hello_world():
    return render_template('index.html')  
    
@app.route('/dojo')  
def dojo():
    return 'Dojo!!'  # Return the string 'Hello World!' as a response
 
@app.route('/say/<name>')  
def say_name(name):
    return 'Hi,  ' + ' ' +name  # Return the string 'Hello World!' as a response
 
@app.route('/say/<integ>/<name>')  
def say_word(integ, name):
    return 'Hi,  ' + ' ' + name  * int(integ) # Return the string 'Hello World!' as a response


    
if __name__=="__main__":
    app.run(debug=True)                   


    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  # Run the app in debug mode.
    # import statements, maybe some other routes
   