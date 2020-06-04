# put your python code here
duration_in_days = int(input())
food_cost_per_day = int(input())
one_way_flight_cost = int(input())
cost_one_night = int(input())

print(food_cost_per_day * duration_in_days + one_way_flight_cost * 2 + cost_one_night * (duration_in_days - 1))
