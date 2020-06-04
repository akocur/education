# put your python code here
hours_start = int(input())
minutes_start = int(input())
seconds_start = int(input())

hours_end = int(input())
minutes_end = int(input())
seconds_end = int(input())

print((hours_end - hours_start) * 3600 + (minutes_end - minutes_start) * 60 + (seconds_end - seconds_start))
