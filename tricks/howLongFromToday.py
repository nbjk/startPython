# use daetime format could be better
import time

# get the current time
current_time_struct = time.localtime()
current_year = current_time_struct[0]
current_month = current_time_struct[1]
current_day = current_time_struct[2]

current_time = time.time() # gain curent time in 'second' format

print "your current time is %s year %s month %s day" % (current_year, current_month, current_day)

# get the time
target_year = int(raw_input('Enter year that you wanted: '))
target_month = int(raw_input('Enter month that you wanted: '))
target_day = int(raw_input('Enter day that you wanted: '))
target_hour = current_time_struct[3]
target_min = current_time_struct[4]
target_sec = current_time_struct[5]
target_wday = current_time_struct[6] # this line may caused mistakes, but here ignore this, because wday, yday, not used in this script
target_yday = current_time_struct[7]
target_isdst = current_time_struct[8]


print "Comfirm your time is %s year %s month %s day" % (target_year, target_month, target_day)

time_list = [target_year, target_month, target_day, target_hour, target_min, target_sec, target_wday, target_yday, target_isdst]

target_time = time.mktime(time_list) # gain target time in 'second' foramt

# calculate
period = target_time - current_time

if period > 0:
    print '%s days from today to that day.' % (int(period/86400) + 1)
    
else:
    print "please check your given time!"
