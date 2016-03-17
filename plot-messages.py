#!/usr/local/bin/python

import datetime
import matplotlib.pyplot as plt
from collections import Counter

dt = datetime.datetime(2000, 12, 31, 16, 0)

with open('message_dates.dat') as f:
    lines = f.read().splitlines()

todate = lambda sec: dt + datetime.timedelta(seconds=int(sec))

dates = [todate(line) for line in lines]
isodates = [date.strftime("%Y-%m-%d") for date in dates]

data = sorted(Counter(isodates).items())

l = range(len(data))
skip = max(len(l) / 20, 1)

print max([(point[1], point[0]) for point in data])

plt.bar(l, [item[1] for item in data], align='center')
plt.xticks(l[::skip], [item[0] for item in data[::skip]], rotation=70)
plt.tight_layout()
plt.show()
