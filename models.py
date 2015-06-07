from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class Country(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(60))

    def __init__(self, Name):
        self.Name = Name

class User(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(120))
    Password = db.Column(db.String(120))
    Name = db.Column(db.String(60))
    DateSignedUp = db.Column(db.TIMESTAMP())

    def __init__(self, Email, Password, Name, DateSignedUp):
        self.Email = Email
        self.Password = Password
        self.Name = Name
        self.DateSignedUp = DateSignedUp

class User_Countries(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Userid = db.Column(db.Integer)
    Countryid = db.Column(db.Integer)
    DateStart = db.Column(db.TIMESTAMP())
    Active = db.Column(db.Boolean)

    def __init__(self, Userid, Countryid, DateStart, Active):
        self.Userid = Userid
        self.Countryid = Countryid
        self.DateStart = DateStart
        self.Active = Active

class Racecourses(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(60), unique=True)

    def __init__(self, Name):
        self.Name = Name

class Selections(db.Model): 
    ID = db.Column(db.Integer, primary_key=True)
    Userid = db.Column(db.Integer)
    Racecourseid = db.Column(db.Integer)
    RaceDate = db.Column(db.TIMESTAMP())
    RaceNumber = db.Column(db.Integer)
    First = db.Column(db.Integer)
    Second = db.Column(db.Integer)
    Third = db.Column(db.Integer)
    Fourth = db.Column(db.Integer)
    Winodds = db.Column(db.Integer)
    Favpos = db.Column(db.Integer)
    Favodds = db.Column(db.Integer)
    NoRunners = db.Column(db.Integer)
    __table_args__ = (UniqueConstraint('Userid', 'Racecourseid', 'RaceDate', 'RaceNumber'),
                     )

    def __init__(self, Userid, Racecourseid, RaceDate, RaceNumber, First, Second, Third, Fourth, Winodds, Favpos, Favodds, NoRunners):
        self.Userid = Userid
        self.Racecourseid = Racecourseid
        self.RaceDate = RaceDate
        self.RaceNumber = RaceNumber
        self.First = First
        self.Second = Second
        self.Third = Third
        self.Fourth = Fourth
        self.Winodds = Winodds
        self.Favpos = Favpos
        self.Favodds = Favodds
        self.NoRunners = NoRunner

class RaceDay(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    RaceDate = db.Column(db.TIMESTAMP())
    RaceCourseCode = db.Column(db.Integer)

    def __init__(self, RaceDace, RaceCourseCode):
        self.RaceDace = RaceDace
        self.RaceCourseCode = RaceCourseCode