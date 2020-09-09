# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
m, d, y = input().split(" ")

if m[0] == "0":
    m = m[1]
if d[0] == "0":
    d = d[1]


day = calendar.weekday(int(y), int(m), int(d))
weekday = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY",
           3: "THRUSHDAY", 4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"}
print(weekday[day])
