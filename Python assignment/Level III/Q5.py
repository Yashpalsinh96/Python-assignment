class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_hours = self.hours + other_time.hours
        total_minutes = self.minutes + other_time.minutes

        total_hours += total_minutes // 60
        total_minutes %= 60

        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes} min")

time1 = Time(3, 50)
time2 = Time(2, 20)

result_time = time1.addTime(time2)
result_time.displayTime()  
result_time.displayMinute()
