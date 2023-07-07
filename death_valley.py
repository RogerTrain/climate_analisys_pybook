from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('death_valley_2021_full.csv')
lines = path.read_text().splitlines()
first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')

reader = csv.reader(lines)
head_row = next(reader)
print(head_row)

highs, lows, date = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print(f'Missing data {current_date}')
    else:
        highs.append(high)
        lows.append(low)
        date.append(current_date)

path2 = Path('sitka_weather_2021_simple.csv')
lines2 = path2.read_text().splitlines()

reader2 = csv.reader(lines2)
head_row2 = next(reader2)
print(head_row2)

highs2, date2 = [], []
for row in reader2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high2 = int(row[4])
    except ValueError:
        print(f'Missing data {current_date}')
    else:
        highs2.append(high2)
        date2.append(current_date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(date, highs, color='red', alpha=0.5, label='Death Valley')
ax.plot(date2, highs2, color='blue', alpha=0.5, label='Sitka')
ax.fill_between(date, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily High Temperature Comparison\nDeath Valley, CA and Sitka"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.legend()

plt.show()
