from app import db

class Customer(db.Model):
    __tablename__ = "customer"
    CustomerId = db.Column(db.Integer, primary_key=True, nullable=False)
    Username = db.Column(db.String(45), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    ConfirmPassword = db.Column(db.String(45), nullable = False)
    Email = db.Column(db.String(100), nullable=False)
    PhoneNumber = db.Column(db.String(11), nullable=False)
    DateOfBirth = db.Column(db.Date, nullable=False)

    def __init__(self, Username, Password, ConfirmPassword, Email, PhoneNumber, DateOfBirth):
        self.Username = Username
        self.Password = Password
        self.ConfirmPassword = ConfirmPassword
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.DateOfBirth = DateOfBirth

class HotelBooking(db.Model):
    __tablename__ = "hotel_booking"
    HotelBookingId = db.Column(db.Integer, primary_key=True, nullable=False)
    CustomerId = db.Column(db.Integer, db.ForeignKey("customer.CustomerId"), nullable=False)
    RoomType = db.Column(db.String(45), nullable=False)

    customer = db.relationship("Customer", foreign_keys= [CustomerId])

    def __init__(self, HotelBookingId, CustomerId, RoomType):
        self.HotelBookingId = HotelBookingId
        self.CustomerId = CustomerId
        self.RoomType = RoomType

class ZooBooking(db.Model):
    __tablename__ = "zoo_booking"
    ZooBookingId = db.Column(db.Integer, primary_key=True, nullable=False)
    CustomerId = db.Column(db.Integer, db.ForeignKey("customer.CustomerId"), nullable=False)
    TicketType = db.Column(db.String(45), nullable=False)

    customer = db.relationship("Customer", foreign_keys= [CustomerId])

    def __init__(self, ZooBookingId, CustomerId, TicketType):
        self.ZooBookingId = ZooBookingId
        self.CustomerId = CustomerId
        self.TicketType = TicketType

class BookingDetails(db.Model):
    __tablename__ = "booking_details"
    HotelBookingId = db.Column(db.Integer, db.ForeignKey("hotel_booking.HotelBookingId"), primary_key=True, nullable=False)
    ZooBookingId = db.Column(db.Integer, db.ForeignKey("zoo_booking.ZooBookingId"), nullable=False)
    BookingDate = db.Column(db.String(45), nullable=False)

    zoo_booking = db.relationship("ZooBooking", foreign_keys= [ZooBookingId])

    def __init__(self, HotelBookingId, ZooBookingId, BookingDate):
        self.HotelBookingId = HotelBookingId
        self.ZooBookingId = ZooBookingId
        self.BookingDate = BookingDate
