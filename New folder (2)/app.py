from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Home():  # put application's code here
    return render_template("Home.html")
@app.route('/Booking')
def Booking():  # put application's code here
    return render_template("Booking.html")
@app.route('/ContactUs')
def ContactUs():  # put application's code here
    return render_template("ContactUs.html")
@app.route('/LogIn')
def LogIn():  # put application's code here
    return render_template("LogIn.html")
@app.route('/SignUp')
def SignUp():  # put application's code here
    return render_template("SignUp.html")
@app.route('/Map')
def Map():  # put application's code here
    return render_template("Map.html")
@app.route('/Animals')
def Animals():  # put application's code here
    return render_template("Animals.html")

@app.route('/Experiences')
def Experiences():  # put application's code here
    return render_template("Experiences.html")

@app.route('/Account')
def Account():  # put application's code here
    return render_template("Account.html")

if __name__ == '__main__':
    app.run()
