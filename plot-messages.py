#!/usr/bin/env python
import datetime
import matplotlib.pyplot as plt


def dayrange(start_date, end_date):
    dates = {}
    day_delta = end_date - start_date
    for n in xrange(day_delta.days + 1):
        dates[start_date + datetime.timedelta(days=n)] = 0
    return dates

epoch = datetime.datetime(2000, 12, 31, 16, 0)

with open('message_dates.dat') as f:
    lines = f.read().splitlines()

todate = lambda sec: epoch + datetime.timedelta(seconds=int(sec))
raw_dates = [todate(line).date() for line in lines]

print "Min: {}".format(min(raw_dates))
print "Max: {}".format(max(raw_dates))

dates = dayrange(min(raw_dates), max(raw_dates))

for raw_date in raw_dates:
    dates[raw_date] += 1

for date in dates:
    date = date.strftime("%Y-%m-%d")

date_list = sorted(dates)

# Graph rendering stuff
l = range(len(date_list))
skip = int(max(len(l) / 20, 1))

print("Max: {0}".format(max([(dates[point], point) for point in dates])))

plt.bar(l, [dates[day] for day in date_list], align='center')
plt.xticks(l[::skip],
           [key for key in date_list[::skip]], rotation=70)
plt.tight_layout()
plt.show()
