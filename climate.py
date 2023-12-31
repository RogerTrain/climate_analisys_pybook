from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
print(first_date)
path = Path('sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
# Extract high temperatures.
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = row[3]
    low = row[4]
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
print(highs)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
