class Time:
	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def get_hours(self):
		return self.hours

	def get_minutes(self):
		return self.minutes

	def get_seconds(self):
		return self.seconds

	def add(self, other_time):
		total_seconds = self.seconds + other_time.seconds
		total_minutes = self.minutes + other_time.minutes
		total_hours = self.hours + other_time.hours

		if total_seconds >= 60:
			total_seconds -= 60
			total_minutes += 1

		if total_minutes >= 60:
			total_minutes -= 60
			total_hours += 1

		return Time(total_hours, total_minutes, total_seconds)

	def subtract(self, other_time):
		total_seconds = self.seconds - other_time.seconds
		total_minutes = self.minutes - other_time.minutes
		total_hours = self.hours - other_time.hours

		if total_seconds < 0:
			total_seconds += 60
			total_minutes -= 1

		if total_minutes < 0:
			total_minutes += 60
			total_hours -= 1

		return Time(total_hours, total_minutes, total_seconds)

	def get_in_24h_format(self):
		return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

time1 = Time(10, 30, 45)
time2 = Time(1, 15, 20)

print("Time 1:", time1.get_hours(), "hours", time1.get_minutes(), "minutes", time1.get_seconds(), "seconds")

sum_time = time1.add(time2)
print("Sum of Time 1 and Time 2:", sum_time.get_in_24h_format())

diff_time = time1.subtract(time2)
print("Difference of Time 1 and Time 2:", diff_time.get_in_24h_format())
