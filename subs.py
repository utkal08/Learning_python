import datetime
import math

current_subs = 10000
goal_subs  =100000
subs_to_go =goal_subs-current_subs
avg_subs_day =500


days_to_go=math.ceil(subs_to_go/avg_subs_day)



star_date =datetime.date.today()
print(star_date + datetime.timedelta(days=days_to_go))


