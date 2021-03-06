from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint,ForeignKey, UniqueConstraint, CheckConstraint, Column
from sqlalchemy.types import Float, Unicode, BigInteger, Integer, Boolean, Date, DateTime, Unicode, DECIMAL, String
from sqlalchemy.orm import relationship, backref
from app import db

# class Country(db.Model):
#     __tablename__ = "Country"
#     ID = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String(60))

#     def __init__(self, Name):
#         self.Name = Name

class User(db.Model):
    __tablename__ = "User"
    ID = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(120))
    Password = db.Column(db.String(120))
    Name = db.Column(db.String(60))
    Animal = db.Column(db.String(60))
    DateSignedUp = db.Column(db.TIMESTAMP())
    performances = relationship("UserPerformance")
    __table_args__ = (UniqueConstraint('Name', 'Animal'),)

    def __init__(self, Email, Password, Name, DateSignedUp, Animal):
        self.Email = Email
        self.Password = Password
        self.Name = Name
        self.DateSignedUp = DateSignedUp
        self.Animal = Animal

# class User_Countries(db.Model):
#     __tablename__ = "User_Countries"
#     ID = db.Column(db.Integer, primary_key=True)
#     Userid = db.Column(db.Integer)
#     Countryid = db.Column(db.Integer)
#     DateStart = db.Column(db.TIMESTAMP())
#     Active = db.Column(db.Boolean)

#     def __init__(self, Userid, Countryid, DateStart, Active):
#         self.Userid = Userid
#         self.Countryid = Countryid
#         self.DateStart = DateStart
#         self.Active = Active

# class Racecourses(db.Model):
#     __tablename__ = "Racecourses"
#     ID = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String(60), unique=True)

#     def __init__(self, Name):
#         self.Name = Name

#separate class for Napoleon based on RaceDay

class Selection(db.Model):
    __tablename__ = "Selection" 
    ID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer,ForeignKey('User.ID'))
    RaceID = db.Column(db.Integer, ForeignKey('Race.ID'))
    # Racecourseid = db.Column(db.Integer) 
    # RaceDate = db.Column(db.TIMESTAMP())
    # RaceNumber = db.Column(db.Integer)
    First = db.Column(db.Integer)
    Second = db.Column(db.Integer)
    Third = db.Column(db.Integer)
    Fourth = db.Column(db.Integer)
    SubmittedAt = db.Column(db.DateTime)
    __table_args__ = (UniqueConstraint('UserID', 'RaceID'),)

    def __init__(self, UserID, RaceID, First, Second, Third, Fourth, SubmittedAt):
        self.UserID = UserID
        self.RaceID = RaceID
        # self.RaceDate = RaceDate
        # self.RaceNumber = RaceNumber
        self.First = First
        self.Second = Second
        self.Third = Third
        self.Fourth = Fourth
        self.SubmittedAt = SubmittedAt


class RaceDay(db.Model):
    __tablename__ = "RaceDay"
    ID = db.Column(db.Integer, primary_key=True)
    RaceDate = db.Column(db.TIMESTAMP())
    RaceCourseCode = db.Column(db.String(5))
    races = relationship('Race')

    def __init__(self, RaceDate, RaceCourseCode):
        self.RaceDate = RaceDate
        self.RaceCourseCode = RaceCourseCode

# 1Race: Many runners
#BASIC RUNNER MODEL USED FOR SELECTIONS
## BIG RUNNER MODEL RunnerExt
class Runner(db.Model):
    __tablename__ = "Runner"
    ID = db.Column(db.Integer, primary_key=True)
    RaceID = db.Column(db.Integer, ForeignKey('Race.ID'))
    HorseNumber = db.Column(db.Integer)
    HorseCode = db.Column(db.String(10))
    HorseName = db.Column(db.String(60))
    JockeyCode = db.Column(db.String(10))
    TrainerCode = db.Column(db.String(10))
    __table_args__ = (UniqueConstraint('RaceID', 'HorseCode'),)

    def __init__(self, RaceID, HorseNumber, HorseCode, HorseName, JockeyCode, TrainerCode):
        self.RaceID = RaceID 
        self.HorseNumber = HorseNumber 
        self.HorseCode = HorseCode 
        self.HorseName = HorseName 
        self.JockeyCode = JockeyCode 
        self.TrainerCode = TrainerCode

class Race(db.Model):
    __tablename__ = "Race"
    ID = db.Column(db.Integer, primary_key=True)
    RaceDate = db.Column(db.TIMESTAMP())
    RaceCourseCode = db.Column(db.String(2))
    RaceName = db.Column(db.String(150))
    RaceDayID = db.Column(db.Integer, ForeignKey('RaceDay.ID'))
    RaceNumber = db.Column(db.Integer)
    RaceType = db.Column(db.String(10))  #CLASS ABBFORM 4S 3 HKG1 G1 Gr
    RaceGoing = db.Column(db.String(10)) #GF GY Y 
    RaceRating = db.Column(db.String(10)) #80-60
    RaceSurface = db.Column(db.String(5)) #AWT or C+3 A 
    RaceDistance = db.Column(Integer) # 1000
    UTCRaceTime = db.Column(db.TIMESTAMP()) #exact jump time updatable
    TrackWidth = db.Column(db.Float)
    Result = db.Column(db.String(20))
    R1 = db.Column(db.Integer)
    R2 = db.Column(db.Integer)
    R3 = db.Column(db.Integer)
    R4 = db.Column(db.Integer)
    WinOdds = db.Column(db.Float)
    FavPos = db.Column(db.Integer)
    FavOdds = db.Column(db.Float)
    NoRunners = db.Column(db.Integer) #count runners
    TrioDiv = db.Column(db.Float)
    TierceDiv = db.Column(db.Float)
    F4Div = db.Column(db.Float)
    QuartetDiv = db.Column(db.Float)
    runners = relationship("Runner")

    def __init__(self, RaceDayID, RaceDate, RaceCourseCode, RaceNumber, Result, WinOdds, FavPos, FavOdds, NoRunners, R1, R2, R3, R4):
        self.RaceDayID = RaceDayID
        self.RaceDate = RaceDate
        self.RaceCourseCode = RaceCourseCode
        self.RaceNumber = RaceNumber
        self.Result = Result
        self.WinOdds = WinOdds
        self.FavPos = FavPos
        self.FavOdds = FavOdds
        self.NoRunners = NoRunners
        self.R1 = R1
        self.R2 = R2
        self.R3 = R3
        self.R4 = R4


    # def __init__(self, RaceDate, RaceCourseCode, RaceNumber, Result, WinOdds, FavPos, FavOdds, NoRunners, RaceName=None, RaceType=None, RaceGoing=None, RaceRating=None, \
    #     RaceSurface=None, UTCRaceTime=None, TrackWidth=None, RaceDayID=None, TrioDiv=None, TierceDiv=None, F4Div=None, QuartetDiv=None):
    #     self.RaceDate = RaceDate
    #     self.RaceCourseCode = RaceCourseCode
    #     self.RaceNumber = RaceNumber
    #     self.Result = Result
    #     self.WinOdds = WinOdds
    #     self.FavPos = FavPos
    #     self.FavOdds = FavOdds
    #     self.NoRunners = NoRunners
    #     self.RaceType = RaceType
    #     self.RaceGoing = RaceGoing
    #     self.RaceRating = RaceRating
    #     self.RaceSurface = RaceSurface
    #     self.UTCRaceTime = UTCRaceTime
    #     self.TrackWidth = TrackWidth
    #     self.RaceName = RaceName
    #     self.RaceDayID = RaceDayID
    #     self.TrioDiv = TrioDiv
    #     self.TierceDiv = TierceDiv
    #     self.F4Div = F4Div
    #     self.QuartetDiv = QuartetDiv 

class Naps(db.Model):
    __tablename__ = "Naps"
    ID = Column(BigInteger, primary_key = True, autoincrement = True, nullable = False)
    RaceDayID = db.Column(db.Integer, ForeignKey('RaceDay.ID'))
    RaceNumberSelection = db.Column(db.String(10))
    UserID = db.Column(db.Integer,ForeignKey('User.ID'))
    RaceID = db.Column(db.Integer, ForeignKey('Race.ID'))
    isWin = db.Column(db.Boolean)

    def __init__(self, RaceDayID, RaceNumberSelection, UserID, RaceID, isWin):
        self.RaceDayID = RaceDayID
        self.RaceNumberSelection = RaceNumberSelection
        self.UserID = UserID
        self.RaceID = RaceID
        self.isWin =  isWin

#SELECTIONGGREGATES
#user:user_performances 1:M performance updated after each meeting
class UserPerformance(db.Model):
    __tablename__ = "UserPerformance"
    ID = Column(BigInteger, primary_key = True, autoincrement = True, nullable = False) # Unique ID
    RaceDate = db.Column(Date, nullable=False)
    UserID = db.Column(db.Integer, ForeignKey('User.ID'))
    Winpc = db.Column(Float, nullable=False)
    Wins = db.Column(Integer)
    TotalWinOdds = db.Column(Float)
    Losses = db.Column(Integer)
    NonRunners = db.Column(Integer)
    MaxSeqWin = db.Column(Integer)
    MaxSeqLose = db.Column(Integer)
    PresSeqWin = db.Column(Integer)
    PresSeqLose = db.Column(Integer)
    MonthRoi = db.Column(Float)
    SeasonRoi = db.Column(Float)
    SeasonWins = db.Column(Integer)
    SeasonLosses = db.Column(Integer)
    NapsWins = db.Column(Integer)
    NapsLosses = db.Column(Integer)
    NapsWinpc = db.Column(Float)
    NapsMaxSeqWin = db.Column(Integer)
    NapsMaxSeqLose = db.Column(Integer)
    NapsPresSeqWin = db.Column(Integer)
    NapsPresSeqLose = db.Column(Integer)
    AvgWinOdds = db.Column(Float, nullable=False)
    Kelly_L200 = db.Column(Float)
    Kelly_Season = db.Column(Float)
    Placepc = db.Column(Float, nullable=False)
    Tiercepc = db.Column(Float)
    AvgTierceOdds = db.Column(Float)
    Triopc = db.Column(Float)
    AvgTrioOdds = db.Column(Float)
    F4pc = db.Column(Float)
    QTTpc = db.Column(Float)
    AvgF4Odds = db.Column(Float)

    #INIT


#ODDS
#THESE 2 TABLES SHOULD EXIST ALREADY - reflect?
##if reflect then:


class HKOddsModel(db.Model):
    __tablename__ = "hk_odds"
    id = Column(BigInteger, primary_key = True, autoincrement = True, nullable = False) # Unique ID
    race_date = Column("racedate", Date, nullable = False) # Race date.
    race_course_code = Column("racecoursecode", Unicode(2)) # Race course code.
    race_number = Column("racenumber", Integer) # Race number.
    horse_number = Column("horsenumber", Integer, nullable = False) # Horse number.
    update_date_time = Column("updatedate", DateTime, nullable = False) # Date and time of last update.
    win_odds = Column("winodds", DECIMAL(10,2)) # Odds of win. It's not float! Float for money is not acceptable!
    is_win_fav = Column("isWinFav", Integer) # Some times this parameter can takes value 2 and more.
    place_odds = Column("placeodds", DECIMAL(10,2)) # The same as Win odds.
    is_place_fav = Column("isPlaceFav", Integer) # The same as is_win_fav.
    pool = Column("pool", BigInteger) # Pool number.
    is_reserve = Column("isReserve", Boolean) # Reserve data.
    is_scratched = Column("isScratched", Boolean) # Scratched data.

    def __init__(self, race_date, race_course_code, race_number, horse_number, update_date_time, win_odds, is_win_fav, place_odds, is_place_fav, pool, is_reserve = False, is_scratched = False):
        self.race_date = race_date
        self.race_course_code = race_course_code
        self.race_number = race_number
        self.horse_number = horse_number
        self.update_date_time = update_date_time
        self.win_odds = win_odds
        self.is_win_fav = is_win_fav
        self.place_odds = place_odds
        self.is_place_fav = is_place_fav
        self.pool = pool
        self.is_reserve = is_reserve
        self.is_scratched = is_scratched


##ODDS
class HKOddsDisplayModel(db.Model):
    __tablename__ = "hk_odds_display"
    ID = db.Column(db.Integer, primary_key=True)
    RaceDate = db.Column(db.TIMESTAMP())
    RaceCourseCode = db.Column(db.String(2))
    RaceNumber = db.Column(db.Integer)
    HorseNumber = db.Column(db.Integer)
    OpWin = db.Column(db.Float)
    OpWinRank = db.Column(db.Integer)
    Win12am = db.Column(Float)
    Win6am  = db.Column(Float)
    Win8am = db.Column(Float)
    Win3pm = db.Column(Float)
    Win5mins = db.Column(Float)
    WinNow = db.Column(Float)
    WinNowRank = db.Column(db.Integer)
    WinNowOPDiff = db.Column(Float)
    WinNowL5minsDiff = db.Column(Float)
    WinNowBettingLine = db.Column(Float)
    WinSp = db.Column(Float)
    WinSpRank = db.Column(db.Integer)

    def __init__(self,RaceDate,RaceCourseCode,RaceNumber,HorseNumber,OpWin,OpWinRank,Win12am,Win6am,Win8am,Win3pm,WinL5mins,WinNow,WinNowRank,WinSp,WinSpRank):
        self.RaceDate = RaceDate
        self.RaceCourseCode = RaceCourseCode
        self.RaceNumber = RaceNumber
        self.HorseNumber = HorseNumber
        self.OpWin = OpWin
        self.OpWinRank = OpWinRank
        self.Win12am = Win12am
        self.Win6am = Win6am
        self.Win8am = Win8am
        self.Win3pm = Win3pm
        self.WinL5mins = WinL5mins
        self.WinNow = WinNow
        self.WinNowRank = WinNowRank
        self.WinSp = WinSp
        self.WinSpRank= WinSpRank
        self.WinNowOPDiff = WinNowOPDiff
        self.WinNow5minsDiff = WinNow5minsDiff
        self.WinNowBettingLine = WinNowBettingLine

class Tipster(db.Model):
    __tablename__ = "TipsterPerformance"
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40))
    TipsterScore = db.Column(db.Float) 
    NumberWinners = db.Column(db.Integer)
    Seconds = db.Column(db.Integer)
    Thirds = db.Column(db.Integer)
    Fourths = db.Column(db.Integer)
    TotalRaces = db.Column(db.Integer)
    WinStrikeRate = db.Column(db.Float)
    NumberFavorites = db.Column(db.Integer)
    PerformanceSequence = db.Column(db.TEXT())
    MaxLosingStreak = db.Column(db.Integer)
    MinWinningStreak = db.Column(db.Integer)
    Last10 = db.Column(db.String(40))

    def __init__(self, Name, TipsterScore, NumberWinners, Seconds, Thirds, Fourths, TotalRaces, WinStrikeRate, NumberFavorites,
        PerformanceSequence, MaxLosingStreak, MinWinningStreak, Last10):
        self.Name = Name
        self.TipsterScore = TipsterScore
        self.NumberWinners = NumberWinners
        self.Seconds = Seconds
        self.Thirds = Thirds
        self.Fourths = Fourths
        self.TotalRaces = TotalRaces
        self.WinStrikeRate = WinStrikeRate
        self.NumberFavorites = NumberFavorites
        self.PerformanceSequence = PerformanceSequence
        self.MaxLosingStreak = MaxLosingStreak
        self.MinWinningStreak = MinWinningStreak
        self.Last10 = Last10
        