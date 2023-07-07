from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('sitka_weather_2021_full.csv')
line = path.read_text().splitlines()

reader = csv.reader(line)
head_row = next(reader)
print(head_row)
date, precipt = [],[]

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        precipts = float(row[5])
    except ValueError:
        print(f'date missing {current_date}')
    else:
        date.append(current_date)
        precipt.append(precipts)
    
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(date,precipt, color = 'green')

title = plt.title("Daily rains in Sitka")
    
plt.show()