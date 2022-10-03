class Time:

    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def gethours(self):
        return self.hour
    def getminutes(self):
        return self.minute
    def getseconds(self):
        return self.second

    def tostring(self):
        return "hours: " + str(self.hour) + " minutes: " + str(self.minute) + " seconds: " + str(self.second)

    def timeinseconds(self):
        return (self.hour * 3600) + (self.minute * 60) + self.second

    def changethetime(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def twelvehourclock(self):

        if self.hour > 12:  # checks if time will be am or pm
            return self.hour - 12, ":", self.minute, ":", self.second, "pm"
        elif self.hour == 0:
            return "12:", self.minute, ":", self.second, "am"
        elif self.hour < 12:
            return self.hour, ":", self.minute, ":", self.second, "am"
        else:
            return self.hour, ":", self.minute, ":", self.second, "pm"

    def whattimeisit(self):
        if 6 <= self.hour < 12:  # determines time of day based off hours
            return "morning"
        elif 12 <= self.hour < 17:
            return "afternoon"
        elif 17 <= self.hour < 22:
            return "evening"
        else:
            return "nighttime"

    def compareto(self, t):
        return self.timeinseconds() - t.timeinseconds()

    def timetill(self, t):
        if self.hour > t.hour:  # determines which time is later
            h = self.hour - t.hour
            m = self.minute - t.minute
            s = self.second - t.second
        else:
            h = t.hour - self.hour
            m = t.minute - self.minute
            s = t.second - self.second
        x = Time(h, m, s)
        return x
