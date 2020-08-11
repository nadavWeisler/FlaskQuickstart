# Import several functions from flask external library
from flask import Flask, render_template, request, url_for, redirect

# Create new variable called app stored our flask web application
app = Flask(__name__)


# The website is www.XYZ.com/first
@app.route('/first')
def first_site():  # Function named "first_site" activate when we go to www.XYZ.com/first
    return render_template("home_screen.html")  # Present the html file called home_screen (in templates folder)


# The website is www.XYZ.com
@app.route('/', methods=['GET', 'POST'])
def login():  # Function named "login" activate when we go to www.XYZ.com
    if request.method == 'POST':  # If we get information from our user (Submit the form)
        password = request.form['txt']  # create variable "password" and store the input result there
        if password == "1234":  # if the input result is equal to 1234
            return redirect(url_for(first_site))  # Go to home screen
        else:  # Wrong password
            return render_template("login.html")  # Represent login page
    elif request.method == 'GET':  # 'GET' method
        return render_template("login.html")  # Get method, so represent login page


if __name__ == '__main__':  # Whats actually run
    app.run()  # Run our web application
