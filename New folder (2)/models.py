from app import db

class Customer(db.Model):
    __tablename__ = "customer"
    CustomerId = db.Column(db.Integer, primary_key=True, nullable=False)
    Username = db.Column(db.String(45), nullable=False)
    Password = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    DateOfBirth = db.Column(db.Date, nullable=False)

    def __init__(self, CustomerId, Username, Password, Email, DateOfBirth):
        self.CustomerId = CustomerId
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.DateOfBirth = DateOfBirth

class Hotel_Booking(db.Model):
    __tablename__ = "hotel_booking"
    HotelBookingId = db.Column(db.Integer, primary_key=True, nullable=False)
    CustomerId = db.Column(db.String(45), db.ForeignKey("customer.CustomerId"), nullable=False)
    RoomType = db.Column(db.String(45), nullable=False)

    def __init__(self, HotelBookingId, CustomerId, RoomType):
        self.HotelBookingId = HotelBookingId
        self.CustomerId = CustomerId
        self.RoomType = RoomType

class Zoo_Booking(db.Model):
    __tablename__ = "zoo_booking"
    ZooBookingId = db.Column(db.Integer, primary_key=True, nullable=False)
    CustomerId = db.Column(db.String(45), db.ForeignKey("customer.CustomerId"), nullable=False)
    TicketType = db.Column(db.String(45), nullable=False)

    def __init__(self, ZooBookingId, CustomerId, TicketType):
        self.ZooBookingId = ZooBookingId
        self.CustomerId = CustomerId
        self.TicketType = TicketType

class Booking_Details(db.Model):
    __tablename__ = "booking_details"
    HotelBookingId = db.Column(db.Integer, db.ForeignKey("hotel_booking.HotelBookingId"), primary_key=True, nullable=False)
    ZooBookingId = db.Column(db.String(45), db.ForeignKey("zoo_booking.ZooBookingId"), nullable=False)
    BookingDate = db.Column(db.String(45), nullable=False)

    def __init__(self, HotelBookingId, ZooBookingId, BookingDate):
        self.HotelBookingId = HotelBookingId
        self.ZooBookingId = ZooBookingId
        self.BookingDate = BookingDate
