import datetime


current_weight =220
goal_weight = 180

avg_lbs_weak =1.5

start_date= datetime.date.today()
end_date =start_date


while current_weight> goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight-=avg_lbs_weak

print(f'Reached goal in {(end_date-start_date).days//7} weeks')