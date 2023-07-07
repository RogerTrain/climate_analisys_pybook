from pathlib import Path
import csv 
from datetime import datetime #####
import matplotlib.pyplot as plt

path = Path('death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines) 
header_row = next(reader)
print(header_row)

lows,highs,date = [],[],[]

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f'missing data {current_date}')
    else:
        highs.append(high)
        lows.append(low)
        date.append(current_date)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(date, highs, color='red', alpha = 0.5)
ax.plot(date, lows, color = 'blue', alpha = 0.5)
ax.fill_between(date, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
