# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:41:51 2018

@author: Nilton Junior
"""

"""

1 - First 100 minutes in one day are priced at 1 coin per minute

2 - After the first 100 minutes in one day, each minute costs 2 coins per 
minute

3 - All calls are rounded up to the nearest minute. For example: 
    59 sec ~ 1 min, 61 sec ~ 2 min

4 - Calls are billed based on the day when they began. So if a call was 
started at 2014-01-01 23:59:59, then it counts as having started on 2014-01-01

"""

def total_cost(calls):
    
    days = []
    
    for i in calls:
        if not(i[0:10] in days):
            days.append(i[0:10])
    
    minutes = [0] * len(days)
    
    for i in range(len(minutes)):
        for j in calls:
            if j[0:10] == days[i]:
                minutes[i] += int(j[20:])//60 + (int(j[20:]) % 60 > 0)
                print(minutes[i])
    
    cost = [0] * len(minutes)
    
    for i in range(len(cost)):
        if minutes[i] > 100:
            cost[i] = 2*(minutes[i] - 100) + 100
        else:
            cost[i] = minutes[i]
    
    print(cost)
    
    return sum(cost)



total_cost(("2014-01-01 01:12:13 181",
           "2014-01-02 20:11:10 600",
           "2014-01-03 01:12:13 6009",
           "2014-01-03 12:13:55 200"))


total_cost(("2014-02-05 01:00:00 60",
            "2014-02-05 02:00:00 60",
            "2014-02-05 03:00:00 60",
            "2014-02-05 04:00:00 6000"))

