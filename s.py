from datetime import datetime, timedelta

print("== Period Tracker ==")

name = input("Enter your name: ")

last_period = input("Enter first day of last period (YYYY-MM-DD): ")

cycle_length = int(input("Cycle Length (days): "))

period_days = int(input("Period Duration: "))

last_date = datetime.strptime(last_period,"%Y-%m-%d")

next_period = last_date + timedelta(days=cycle_length)

ovulation = next_period - timedelta(days=14)

fertile_start = ovulation - timedelta(days=5)

fertile_end = ovulation + timedelta(days=1)

print("\n---------RESULT---------")

print("Name :",name)

print("Next Period :",next_period.date())

print("Ovulation Day :",ovulation.date())

print("Fertile Window :")

print(fertile_start.date(),"to",fertile_end.date())