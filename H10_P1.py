# python 2
#
# Homework 10, Problem 1
#
# Name: Jeffrey Xiao
#

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year


    def __repr__(self):
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    def isLeapYear(self):
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False
    
    def copy(self):
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
        
    def tomorrow(self):
        fdays = 28 + self.isLeapYear()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.day > DIM[self.month]:
            self.day = 1
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1
    def yesterday(self):
        fdays = 28 + self.isLeapYear()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day -= 1
        if self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.year -= 1
                self.month = 12
            self.day = DIM[self.month]
    def addNDays (self, N):
        for i in range(N):
            self.tomorrow()
    def subNDays (self, N):
        for i in range(N):
            self.yesterday()
    def isBefore (self, d2):
        if d2.year != self.year:
            return self.year < d2.year
        if d2.month != self.month:
            return self.month < d2.month
        return self.day < d2.day
    def isAfter (self, d2):
        if d2.year != self.year:
            return self.year > d2.year
        if d2.month != self.month:
            return self.month > d2.month
        return self.day > d2.day
    def diff (self, d):
        cnt = 0
        d1 = self.copy()
        d2 = d.copy()
        while d1.isBefore(d2):
            d1.tomorrow()
            cnt -= 1
        while d1.isAfter(d2):
            d1.yesterday()
            cnt += 1
        return cnt
    
    def dow (self):
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekday[((2 + self.diff(Date(11, 12, 2014)))%7+7)%7]