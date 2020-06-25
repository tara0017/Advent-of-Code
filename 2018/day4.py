#day4
def sort_by_day(m):
    m = sorted(m, key=lambda m_entry: m_entry[2])
    #print (m)
    return m


def seperate_by_day(m):
    sorted_month_by_day = []
    i = 0
    while i  < len(month):
        day = []
        current_day = month[i][2]
        while month[i][2] == current_day:
            day.append(month[i])
            i += 1
            if i == len(month):
                break
        sorted_month_by_day.append(day)
    return sorted_month_by_day


def update_sleep(g, t):
    #print(g)
    global sleep_tracker
    if g in sleep_tracker:  #guard already slept
        sleep_tracker[g] += t
    else:
        sleep_tracker[g] = t

        
records = []

f = open("day4_input.txt", "r")
for x in f:
    x = x.replace("[", "")
    x = x.replace("]", "")
    x = x.replace("-", " ")
    x = x.replace("00:", "12")
    x = x.replace("23:", "11")
    x = x.replace("#", "")     
    entry = x.split()
    records.append(entry)

records = sorted(records, key=lambda records_entry: records_entry[1])
monthly_record = []


#break the dates by month
i = 0
while i < len(records):
    month = []
    current_month = records[i][1]
    while records[i][1] == current_month:
        month.append(records[i])
        i += 1
        if i == len(records):
            break
    monthly_record.append(month)


#sort each month by the day
for i in range(len(monthly_record)):
    monthly_record[i] = sort_by_day(monthly_record[i])

#break the month up by days
seperated_by_day_monthly_record = []    
for month in monthly_record:        
    m = seperate_by_day(month)
    seperated_by_day_monthly_record.append(m)


#sort each day by time
sorted_data = []
for month in seperated_by_day_monthly_record:
    m = []
    for day in month:
        sorted_day = sorted(day, key=lambda day_entry: day_entry[3])
        m.append(sorted_day)
    sorted_data.append(m)

#find sleepiest guard
sleep_tracker = {}
current_guard = ""
sleep_start = 0
sleep_end   = 0 
for month in sorted_data:  
    for day in month:
        for entry in day:
            if entry[4] == "Guard":
                current_guard = entry[5]
            elif entry[4] == "falls":
                sleep_start = int(entry[3])
            elif entry[4] == "wakes":
                sleep_end = int(entry[3])
                nap_time = sleep_end - sleep_start
                update_sleep(current_guard, nap_time)
                
            
            #print(entry)
    #print("--------------------------")

print(sleep_tracker)
most_sleep = 0
for k,v in sleep_tracker.items():
    if v > most_sleep:
        print(k, v)
        most_sleep = v

#Guard #109 slept 531 minutes


time = []
for i in range(60):
    time.append(0)

current_guard = 0
for month in sorted_data:  
    for day in month:
        for entry in day:
            if entry[4] == "Guard":
                current_guard = entry[5]
            elif entry[4] == "falls" and current_guard == '109':
                print(entry)
                sleep_start = int(entry[3])
            elif entry[4] == "wakes" and current_guard == '109':
                print(entry)
                sleep_end = int(entry[3])
                s = sleep_start % 100
                e = sleep_end   % 100
                for i in range(s, e):
                    time[i] += 1
                print(time)

print(time)
print(time.index(max(time)))
                








