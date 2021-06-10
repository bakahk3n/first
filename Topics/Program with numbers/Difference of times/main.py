# put your python code here
hour = int(input())
minutes = int(input())
seconds = int(input())
time = (hour * 60 * 60) + (minutes * 60) + seconds

hour_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
time_2 = (hour_2 * 60 * 60) + (minutes_2 * 60) + seconds_2

print(time_2 - time)