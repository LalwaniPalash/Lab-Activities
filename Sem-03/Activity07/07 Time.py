class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def total_minutes(self):
        return self.hour * 60 + self.minute

    def __lt__(self, other):
        return self.total_minutes() < other.total_minutes()

    def __gt__(self, other):
        return self.total_minutes() > other.total_minutes()

    def __le__(self, other):
        return self.total_minutes() <= other.total_minutes()

    def __ge__(self, other):
        return self.total_minutes() >= other.total_minutes()

    def __eq__(self, other):
        return self.total_minutes() == other.total_minutes()

    def __ne__(self, other):
        return self.total_minutes() != other.total_minutes()

time1 = Time(5, 30)
time2 = Time(6, 45)
time3 = Time(5, 30)

print("time1 < time2:", time1 < time2)   # Output: True
print("time1 > time2:", time1 > time2)   # Output: False
print("time1 <= time2:", time1 <= time2) # Output: True
print("time1 >= time2:", time1 >= time2) # Output: False
print("time1 == time3:", time1 == time3) # Output: True
print("time1 != time2:", time1 != time2) # Output: True
