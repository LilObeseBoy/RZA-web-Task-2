from flask import session, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

def register_routes(app, db):

    @app.route('/')
    def home():
        return render_template("Home.html")

    @app.route('/Booking', methods=["Get", "POST"])
    def booking():
        if request.method == "POST":
            from models import ZooBooking
            number = int(request.form["number"])
            ticket_type = request.form["ticket_type"]
            for i in range(number):
                new_ticket = ZooBooking(
                    CustomerId = session["customer_id"],
                    TicketType = ticket_type
                )
                db.session.add(new_ticket)
                db.session.commit()
        return render_template("Booking.html")

    @app.route('/ContactUs')
    def contactus():
        return render_template("ContactUs.html")

    @app.route('/LogIn', methods=["GET", "POST"])
    def login():
        customer_id = session.get("customer_id")
        if customer_id != None:
            return redirect(url_for("home"))
        if request.method == "POST":
            login_username = request.form["LogInUsername"]
            login_password = request.form["LogInPassword"]
            from models import Customer
            customer = Customer.query.filter_by(Username = login_username).first()
            if customer and check_password_hash(customer.Password, login_password):
                session["customer_id"] = customer.CustomerId
                session["username"] = customer.Username
                print("Logged in")
                return redirect(url_for("account"))
            else:
                print("failed to log in!")
        return render_template("LogIn.html")

    @app.route('/SignUp', methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            print("do something")
            from models import Customer
            raw_password=request.form["SignUpPassword"]
            hashed_password=generate_password_hash(raw_password,method="pbkdf2:sha256")
            new_customer = Customer(Username=request.form["SignUpUsername"],
                                    Password=hashed_password,
                                    Email=request.form["SignUpEmail"],
                                    PhoneNumber=request.form["SignUpPhoneNumber"],
                                    DateOfBirth=request.form["SignUpDateOfBirth"])
            db.session.add(new_customer)
            db.session.commit()
            return render_template("LogIn.html")
        return render_template("SignUp.html")

    @app.route('/Map')
    def interactivemap():
        return render_template("Map.html")

    @app.route('/Animals')
    def animals():
        return render_template("Animals.html")

    @app.route('/Experiences')
    def experiences():
        return render_template("Experiences.html")

    @app.route('/Account', methods=["GET", "POST"])
    def account():
        if "customer_id" not in session:
            return redirect(url_for("home_page"))
        customer_id = session.get("customer_id")
        from models import ZooBooking
        bookings = ZooBooking.query.filter_by(CustomerId=customer_id).all()
        tickets = []
        for booking in bookings:
            new_tickets = ZooBooking.query.filter_by(TicketType=booking.TicketType).all()
            tickets.extend(new_tickets)
        return render_template("account.html", ZooBooking=tickets, )

    @app.context_processor
    def inject_user():
        return {
            "logged_in": "customer_id" in session,
            "username": session.get("username")
        }

    @app.route('/Logout')
    def logout():
        session.clear()
        return redirect(url_for("home"))

