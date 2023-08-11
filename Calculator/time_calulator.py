class TimeCalculator:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = self.to_seconds(hours, minutes, seconds)

    @staticmethod
    def to_seconds(hours, minutes, seconds):
        return hours * 3600 + minutes * 60 + seconds

    def add_time(self, hours=0, minutes=0, seconds=0):
        self.total_seconds += self.to_seconds(hours, minutes, seconds)

    def subtract_time(self, hours=0, minutes=0, seconds=0):
        self.total_seconds -= self.to_seconds(hours, minutes, seconds)
        self.total_seconds %= 24 * 3600

    def to_12_hour_format(self):
        period = "AM" if self.total_seconds < 12 * 3600 else "PM"
        hours = self.total_seconds // 3600
        if hours > 12:
            hours -= 12
        return f"{hours:02d}:{self.total_seconds // 60 % 60:02d}:{self.total_seconds % 60:02d} {period}"

    def __str__(self):
        hours = self.total_seconds // 3600
        minutes = self.total_seconds // 60 % 60
        seconds = self.total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    # Get user input for initial time
    hours = int(input("Enter the initial hours: "))
    minutes = int(input("Enter the initial minutes: "))
    seconds = int(input("Enter the initial seconds: "))

    time_calculator = TimeCalculator(hours, minutes, seconds)
    print("Initial Time (24-hour format):", time_calculator)
    print("Initial Time (12-hour format):", time_calculator.to_12_hour_format())

    # Get user input for time operation
    operation = input("Enter the operation (add/subtract): ")
    operation = operation.lower()

    if operation == "add":
        hours = int(input("Enter the hours to add: "))
        minutes = int(input("Enter the minutes to add: "))
        seconds = int(input("Enter the seconds to add: "))
        time_calculator.add_time(hours, minutes, seconds)
    elif operation == "subtract":
        hours = int(input("Enter the hours to subtract: "))
        minutes = int(input("Enter the minutes to subtract: "))
        seconds = int(input("Enter the seconds to subtract: "))
        time_calculator.subtract_time(hours, minutes, seconds)
    else:
        print("Invalid operation. Please enter 'add' or 'subtract'.")

    print("Resulting Time (24-hour format):", time_calculator)
    print("Resulting Time (12-hour format):", time_calculator.to_12_hour_format())
